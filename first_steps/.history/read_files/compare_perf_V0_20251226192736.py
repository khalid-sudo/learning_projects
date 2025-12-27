def _is_python_file(file_name: str) -> bool:
    if file_name.endswith('.py'):
        return True
    else:
        return False

def _validate_file_path(file_path: str)-> bool:
    try:
        with open(file_path, 'r'):
    except

def get_script_from_file(file_name: str)-> list:
    if _is_python_file(file_name):
        return 
def run_file():
    ...
def main():
    file = "./data/text.txt"
    try:
        with open(file,"r") as word:
            for line in word:
                print(line)
    except FileNotFoundError:
        print("the file wasn't found")

if __name__ == "__main__":
    main()
