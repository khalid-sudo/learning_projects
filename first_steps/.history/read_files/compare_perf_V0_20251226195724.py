def _is_python_file(file_name: str) -> bool:
    if file_name.endswith('.py'):
        return True
    else:
        return False

def _validate_file_path(file_path: str):
    with open(file_path, 'r') as f:
            return [content for content in f]

def get_script_from_file(file_path: str) -> list:

    try:
        if _is_python_file(file_path):
            return _validate_file_path(file_path)
    except FileNotFoundError as e:
        raise FileNotFoundError("")

def run_file():
    ...
def main():
    file = "./data/main.py"
    try:
        print(get_script_from_file(file))
    except FileNotFoundError as f:
        print(f"{f}")
    except Exception as e:
        print(f"this is what happened {e}")

if __name__ == "__main__":
    main()
