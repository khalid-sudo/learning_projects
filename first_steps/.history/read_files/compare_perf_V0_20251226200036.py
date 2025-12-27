def _is_python_file(file_name: str) -> bool:
    if file_name.endswith('.py'):
        return True
    else:
        return False

def _validate_file_path(file_path: str):
    try:
        with open(file_path, 'r') as f:
                return [content for content in f]
    except OSError as o:
        raise OSError(f"the errors seems to be {o}")

def get_script_from_file(file_path: str) -> list:

    try:
        if _is_python_file(file_path):
            return _validate_file_path(file_path)
    except Os as e:
        raise FileNotFoundError(f"the File with the name {file_path} wasn't found see {e}")

def run_file():
    ...
def main():
    file = "./data/man.py"
    try:
        print(get_script_from_file(file))
    except Exception as e:
        print(f"this is what happened {e}")

if __name__ == "__main__":
    main()
