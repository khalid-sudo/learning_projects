def _is_python_file() -> bool:
    ...
def get_script_from_file():
    ...
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
