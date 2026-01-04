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
    if isinstance(value,list) and len(value)>0:
        return read_parsed(value[0])
    elif isinstance(value,ast.AST):
        for valu in ast.iter_child_nodes(value):
            print(f"************{value.__dict__}")
            for k,v in value.__dict__.items():
                if isinstance(v,list) and len(v)>0:
                    return read_parsed(v[0])
                elif not isinstance(v, ast.AST):
                    print(f"Chiled Node {valu} key=> {k} and it's value is {v}") 
                elif isinstance(v, ast.AST):
                    print(v.__dict__)
                    return read_parsed(v)
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
                if isinstance(value, ast.AST):
                    print(f"the argument {value.__dict__}")
                    for k,v in value.__dict__.items():
                        if isinstance(v,list) and len(v) > 0 and isinstance(v[0], ast.AST):
                            for ke,va in v[0].__dict__.items():
                                print(f"the argument {k}  has the {ke} within the  {va}")
                                if isinstance(va,list) and len(va) > 0 and isinstance(va[0], ast.AST):
                                    print("dkhaal")
                                    for key,val in va[0].__dict__.items():
                                        print(f"which has  {ke}  has {key} within the  {val}")
                                elif isinstance(va, ast.AST) :
                                    for key,val in va.__dict__.items():
                                        print(f"which has {ke}  has {key} within the {val}")
                        elif isinstance(v, ast.AST):
                            for k,v in v.__dict__.items():
                                if isinstance(v,list) and len(v) > 0 and isinstance(v[0], ast.AST):
                                    for ke,va in v[0].__dict__.items():
                                        print(f"the argument {k}  has the {ke} with the {va}")
                                        if isinstance(va,list) and len(va) > 0 and isinstance(va[0], ast.AST):
                                            for key,val in va[0].__dict__.items():
                                                print(f"twhich   has {key} within {val}")
                                        elif isinstance(va, ast.AST) :
                                            for key,val in va.__dict__.items():
                                                print(f"which has  {ke}  has indeed {key} with {val}")
                                else:
                                    print(f"the key is {k} the value {v}")
                                
                elif isinstance(value,list) and len(value) > 0 and isinstance(value[0], ast.AST):
                    for k,v in value[0].__dict__.items():
                        if isinstance(v,list) and len(v) > 0 and isinstance(v[0], ast.AST):
                            for ke,va in v[0].__dict__.items():
                                print(f"the argument {k}  has the {ke} with the {va}")
                                if isinstance(va,list) and len(va) > 0 and isinstance(va[0], ast.AST):
                                   
                                    for key,val in va[0].__dict__.items():
                                        print(f"twhich   has {key} within {val}")
                                elif isinstance(va, ast.AST) :
                                    for key,val in va.__dict__.items():
                                        print(f"which has  {ke}  has indeed {key} with {val}")
                        elif isinstance(v, ast.AST):
                            print("hina sa askoto 9alilan")
                            for k,v in v.__dict__.items():
                                if isinstance(v,list) and len(v) > 0 and isinstance(v[0], ast.AST):
                                    for ke,va in v[0].__dict__.items():
                                        print(f"the argument {k}  has the {ke} with the {va}")
                                        if isinstance(va,list) and len(va) > 0 and isinstance(va[0], ast.AST):
                                        
                                            for key,val in va[0].__dict__.items():
                                                print(f"which   has {key} within {val}")
                                        elif isinstance(va, ast.AST) :
                                            for key,val in va.__dict__.items():
                                                print(f"which has  {ke}  has indeed {key} with {val}")
                
    except Exception as e:
        logging.info(f"{e}")

def main():
    file_path:str = "../data/test2.py"
    parse_file(file_path)

main()

