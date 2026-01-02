from pathlib import Path
import ast
import logging
logging.basicConfig(level=logging.INFO)
def read_file(file_name: Path) -> str:
    return file_name.read_text()
def parse_file(file_name:str):
    try:
        source_code = read_file(Path(file_name))
        print(f"the result is {ast.dump(ast.parse(source_code,filename=file_name,mode="exec",type_comments=True,feature_version=(3, 13)))}")
    except Exception as e:
        logging.info(f"{e}")
def main():
    file_path:str = "../data/test1.py"
    parse_file(file_path)

main()

