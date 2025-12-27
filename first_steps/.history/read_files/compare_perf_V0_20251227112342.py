import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"The function {func.__name__!r} took: {end_time - start_time:.4f} sec")
        return result
    return wrapper
def _is_python_file(file_name: str) -> bool:
    if file_name.endswith('.py'):
        return True
    else:
        return False

def _validate_file_path(file_path: str):
    try:
        with open(file_path, 'r') as f:
                return f.read()
    except OSError as o:
        raise OSError(f"the errors seems to be {o}")

def get_script_from_file(file_path: str) -> str:
    if  not _is_python_file(file_path):
            raise ValueError("the file provided is not a python variable")
    try:
        return _validate_file_path(file_path)
    except OSError as e:
        raise FileNotFoundError(f"the File with the name {file_path} wasn't found . {e}")

def run_file(file_content: str):
    ...
def main():
    file = "./data/main.py"
    try:
        print(get_script_from_file(file))
    except Exception as e:
        print(f"this is what happened {e}")

if __name__ == "__main__":
    main()
