from pathlib import Path
import ast
import logging
from types import GeneratorType, NoneType
import types
from typing import Generator
logging.basicConfig(level=logging.INFO)

def read_file(file_name: Path) -> str:
    return file_name.read_text()

def read_parsed(value):
        if isinstance(value, ast.AST):
            for key,val in value.__dict__.items():
                if isinstance(val,(ast.AST,list)):
                    read_parsed(val)
                else:
                    print(f"$$which has {key} with value =>{val}") 
        elif isinstance(value,list) and len(value)>0  and isinstance(value[0], ast.AST):
             for key,val in value[0].__dict__.items():
                if isinstance(val,(ast.AST,list)):
                    read_parsed(val)
                else:
                    print(f"**which has {key} with value => {val}") 
        else:
            return f"value => {value}"  



def parse_file(file_name: str):
    try:
        source_code = read_file(Path(file_name))
        tree = ast.parse(source_code,filename=file_name,mode="exec",type_comments=True,feature_version=(3, 13))
        #print(ast.dump(tree))
        tree = ast.parse(source_code)
        #assignment_node = tree.body
        for node in tree.body:
            for field_name, value in ast.iter_fields(node):
                #print(f"the field name is {field_name} and it's value is {read_parsed(value)}")
                print(f"the field name is {field_name} and it's value is {value}")
                print(read_parsed(value))
    except Exception as e:
        logging.info(f"{e}")

def main():
    file_path:str = "../data/test2.py"
    parse_file(file_path)

main()

