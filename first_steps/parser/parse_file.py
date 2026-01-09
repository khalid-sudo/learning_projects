from pathlib import Path
import ast
import logging
from sys import version_info
from .visualize_parser import  visualizer
from pyvis.network import Network

logging.basicConfig(level=logging.INFO)
_net = visualizer.net

def read_file(file_name: Path) -> str:
    return file_name.read_text()


def __read_parsed(value):
        if isinstance(value, ast.AST):
            for key,val in value.__dict__.items():
                if isinstance(val,(ast.AST,list)):
                     read_parsed(val)
                else:
                    if key  not in ["lineno","end_lineno","col_offset","end_col_offset","kind"]:
                        print(f"{key} with value =>{val}")
        elif isinstance(value,list) and len(value)>0  and isinstance(value[0], ast.AST):
            for index in range(len(value)):
                for key,val in value[index].__dict__.items():
                    if isinstance(val,(ast.AST,list)):
                         read_parsed(val)
                    else:
                        if key  not in ["lineno","end_lineno","col_offset","end_col_offset"]:
                           print(f"{key} with value => {val}")
        # else:
        #     return f"value => {value}"  
def read_parsed(value):
        if isinstance(value, ast.AST):
            for key,val in value.__dict__.items():
                if isinstance(val,(ast.AST,list)):
                    yield from read_parsed(val)
                else:
                    if key  not in ["lineno","end_lineno","col_offset","end_col_offset","kind"]:
                        yield f"{key} with value =>{val}"
        elif isinstance(value,list) and len(value)>0  and isinstance(value[0], ast.AST):
            for index in range(len(value)):
                for key,val in value[index].__dict__.items():
                    if isinstance(val,(ast.AST,list)):
                        yield from read_parsed(val)
                    else:
                        if key  not in ["lineno","end_lineno","col_offset","end_col_offset"]:
                           yield f"{key} with value => {val}" 
        # else:
        #     return f"value => {value}"  

def _parse_file(file_name: Path,file_content: str):
    try:
        if file_content:
            tree = ast.parse(file_content,filename=file_name,mode="exec",type_comments=True,feature_version=(version_info.major, version_info.minor))
            #print(ast.dump(tree))
            for node_index in range(len(tree.body)):
                node_id = str(tree.body[node_index])
                print(f"the node is is {node_id}")
                label = type(tree.body[node_index]).__name__+f"{node_index}"
                _net.add_node(node_id, label=label, hidden=True, group="root_children", shape="box")
                _net.add_edge("Root", node_id, arrows="to",arrowStrikethrough=False)
                for field_name, value in ast.iter_fields(tree.body[node_index]):
                    label = type(field_name).__name__
                    content= list(read_parsed(value))
                    print(f"field name is {field_name} value =>{__read_parsed(value)}")
                    if content:
                         _net.add_node(field_name+f"{content}", label=f"{content}",borderWidth=2,margin=15,color={
                             "background": "#2b2b2b", # Dark theme 'Body'
                             "border": "#00ff00",     # Neon green border
                         },hidden=True, group="root_children_of_children",shape="box"
                         )
                         _net.add_edge(node_id, field_name+f"{content}", arrows="to",arrowStrikethrough=False)
                    #print(f"the field name is {field_name} and it's value is {value}")    
        else:
            ...
    except Exception as e:
        logging.info(f"{e}")
    finally:
        #generate_graph
        visualizer.generate_graph(_net)



def main():
    file_path:Path = Path("./parser/visualize_parser.py")
    file_content = read_file(file_path)
    _parse_file(file_content,file_content)
    
if __name__ == "__main__":
    main()

