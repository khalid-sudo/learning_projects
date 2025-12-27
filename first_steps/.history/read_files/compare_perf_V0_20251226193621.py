def _is_python_file(file_name: str) -> bool:
    if file_name.endswith('.py'):
        return True
    else:
        return False

def _validate_file_path(file_path: str) -> list:
    try:
        with open(file_path, 'r') as f:
            return [content for content in f]
    except:
        raise FileNotFoundError()

def get_script_from_file(file_path: str) -> list:
    if _is_python_file(file_path):
        try:
            return _validate_file_path(file_path)
        except FileNotFoundError:
            raise FileNotFoundError()

def run_file():
    ...
def main():
    file = "./data/main.py"
    if get_script_from_file(file):
        print(get_script_from_file(file))

if __name__ == "__main__":
    main()
