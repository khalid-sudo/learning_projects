from pathlib import Path
from resource import *
import time
import logging
import threading
logging.basicConfig(format='%(threadName)s (ID: %(thread)d): %(message)s', level=logging.INFO)
def timer(func) -> ...:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        Usage_stats = getrusage(RUSAGE_SELF)
        print(f"The function {func.__name__} took: {end_time - start_time:.4f} sec\n")
        print("1. CPU Time (The 'Cost' of Execution)\n")
        print(f"your code spent ~{Usage_stats.ru_utime} seconds executing your own Python logic (loops, math, string parsing)\n")
        print(f"the operating system spent ~{Usage_stats.ru_stime} seconds performing tasks on your behalf (like allocating memory or opening files).\n")
        print(f"2. Memory Usage (The 'Space' Occupied) \n")
        print(f"the peak amount of physical RAM your process held at any one time during its execution is {Usage_stats.ru_maxrss}")
        print("3. System Stress & Stability\n")
        print(f"The number of times the process realized a tool was missing and had to walk all the way to the warehouse (Disk) to get it ({Usage_stats.ru_majflt} times).\n")
        return result
    return wrapper

def _is_python_file(file_name: Path) -> Path:
    """checks if the file is a python file and returns Tru when it is a python file"""
    if file_name.suffix == '.py':
        return file_name

def get_script_from_file(file_path: Path) -> str:
    file_content = _is_python_file(file_path)
    if  not file_content:
            raise ValueError("the file provided is not a python file")
    else:
        return file_content.read_text()

@timer
def run_file(file_content: str):
    name = {}
    exec(file_content,name,name)

def main(file_path: Path):
    try:
        run_file(get_script_from_file(file_path))
    except Exception as e:
        print(f"this is what happened {e}")

if __name__ == "__main__":
    logging.info(f"This is running in the {__name__} way.")
    #current_system = sys._current_frames()
    #for key, value in current_system.items():
    #    print(f"the key is {key} and the value globals  is {value.f_globals.items()} \n \t and \n*********************\nlocals  {value.f_locals.items()}")
    thread1 = threading.Thread(target=main,args=(Path("./data/test2.py"),))
    thread2 = threading.Thread(target=main,args=(Path("./data/test1.py"),))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
