from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import uuid
import html
import ast

@dataclass
class DrawIoVisualizer:
    file_content: str
    file_name: Path
    
    def generate_diagram_xml(self, ast_tree: ast.AST) -> str:
        """Generate Draw.io compatible XML with clickable layers for expand/collapse"""
        
        # XML template with layers support
        xml_parts = []
        xml_parts.append('<?xml version="1.0" encoding="UTF-8"?>')
        xml_parts.append('<mxfile host="app.diagrams.net" modified="2024-01-09T12:00:00.000Z" agent="AST Parser" etag="ast-diagram" version="24.0.0" type="device">')
        xml_parts.append('<diagram id="diagram1" name="AST Diagram">')
        xml_parts.append('<mxGraphModel dx="1234" dy="832" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">')
        xml_parts.append('<root>')
        
        # Root cell (required)
        xml_parts.append('<mxCell id="0"/>')
        xml_parts.append('<mxCell id="1" parent="0"/>')
        
        # Define layers for different levels
        xml_parts.append('<mxCell id="layer1" value="Root Level" parent="0"/>')  # Main layer - always visible
        xml_parts.append('<mxCell id="layer2" value="AST Nodes" parent="0"/>')   # Child nodes - toggleable
        xml_parts.append('<mxCell id="layer3" value="Field Details" parent="0"/>')  # Grandchild nodes - toggleable
        
        # Title (on main layer)
        xml_parts.append('<mxCell id="title" parent="layer1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1;" value="AST Parser Diagram" vertex="1"><mxGeometry height="30" width="200" x="325" y="20" as="geometry"/></mxCell>')
        
        # Instructions (on main layer)
        xml_parts.append('<mxCell id="instructions" parent="layer1" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;" value="Click nodes to show/hide child elements" vertex="1"><mxGeometry height="25" width="250" x="50" y="15" as="geometry"/></mxCell>')
        
        # Root node - File content (on main layer)
        root_id = str(uuid.uuid4())[:8]
        filename_str = str(self.file_name.name)
        escaped_filename = html.escape(filename_str)
        escaped_content = html.escape(self.file_content[:150] + "..." if len(self.file_content) > 150 else self.file_content)
        
        xml_parts.append(f'<mxCell id="{root_id}" value="&lt;b&gt;FILE: {escaped_filename}&lt;/b&gt;&lt;br&gt;&lt;i&gt;(Click to show AST nodes)&lt;/i&gt;&lt;br&gt;{escaped_content}" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#2b2b2b;strokeColor=#00ff00;fontColor=white;fontFamily=monospace;fontSize=10;verticalAlign=top;" parent="layer1" vertex="1"><mxGeometry x="350" y="70" width="250" height="120" as="geometry"/></mxCell>')
        
        y_position = 220  # Start position for child nodes
        
        # Add child nodes for each AST node in tree.body (on layer2)
        for node_index, node in enumerate(ast_tree.body):
            node_id = str(uuid.uuid4())[:8]
            
            node_type = type(node).__name__
            node_label = html.escape(f"{node_type}")
            
            # Color coding based on node type
            if node_type == "FunctionDef":
                style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;fontStyle=1;"
            elif node_type == "ClassDef":
                style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#8b4513;strokeColor=#daa520;fontColor=white;fontSize=11;fontStyle=1;"
            elif node_type in ["Import", "ImportFrom"]:
                style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#654321;strokeColor=#daa520;fontColor=white;fontSize=11;"
            elif node_type == "Assign":
                style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;"
            else:
                style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;"
            
            # Add "(Click for details)" to make it clear these are clickable
            clickable_label = f"{node_label}&lt;br&gt;&lt;i style=&quot;font-size:9px;&quot;&gt;(Click for fields)&lt;/i&gt;"
            xml_parts.append(f'<mxCell id="{node_id}" value="{clickable_label}" style="{style}" parent="layer2" vertex="1"><mxGeometry x="150" y="{y_position}" width="140" height="45" as="geometry"/></mxCell>')
            
            # Animated edge from root to child
            edge_id = str(uuid.uuid4())[:8]
            xml_parts.append(f'<mxCell id="{edge_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;strokeWidth=3;strokeColor=#00ff00;flowAnimation=1;" parent="layer2" source="{root_id}" target="{node_id}" edge="1"><mxGeometry relative="1" as="geometry"/></mxCell>')
            
            # Add grandchild nodes for AST fields (on layer3)
            field_y = y_position + 60
            for field_name, value in ast.iter_fields(node):
                field_content = self._extract_field_content(value)
                if field_content:
                    field_id = str(uuid.uuid4())[:8]
                    
                    # Style based on content type
                    if "FunctionDef" in field_content or "def " in field_content:
                        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=10;"
                    elif "ClassDef" in field_content or "class " in field_content:
                        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontSize=10;"
                    elif "Import" in field_content:
                        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=10;"
                    else:
                        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=9;"
                    
                    escaped_field = html.escape(field_content[:80] + "..." if len(field_content) > 80 else field_content)
                    
                    xml_parts.append(f'<mxCell id="{field_id}" value="{escaped_field}" style="{style}" parent="layer3" vertex="1"><mxGeometry x="320" y="{field_y}" width="180" height="35" as="geometry"/></mxCell>')
                    
                    # Animated edge from parent node to field
                    field_edge_id = str(uuid.uuid4())[:8]
                    xml_parts.append(f'<mxCell id="{field_edge_id}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#9673a6;flowAnimation=1;dashed=1;" parent="layer3" source="{node_id}" target="{field_id}" edge="1"><mxGeometry relative="1" as="geometry"/></mxCell>')
                    
                    field_y += 50
            
            y_position += max(140, field_y - y_position + 30)
        
        # Add layer visibility controls (these will appear as checkboxes in Draw.io)
        xml_parts.append('<mxCell id="layer1_visible" value="1" style="shape=checkbox;fillColor=strokeColor;spacingRight=2;" parent="0" vertex="1"><mxGeometry x="10" y="10" width="20" height="20" as="geometry"/></mxCell>')
        xml_parts.append('<mxCell id="layer2_visible" value="0" style="shape=checkbox;fillColor=strokeColor;spacingRight=2;" parent="0" vertex="1"><mxGeometry x="10" y="35" width="20" height="20" as="geometry"/></mxCell>')
        xml_parts.append('<mxCell id="layer3_visible" value="0" style="shape=checkbox;fillColor=strokeColor;spacingRight=2;" parent="0" vertex="1"><mxGeometry x="10" y="60" width="20" height="20" as="geometry"/></mxCell>')
        
        # Layer labels
        xml_parts.append('<mxCell id="layer1_label" value="Show Root" parent="0" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;" vertex="1"><mxGeometry x="35" y="10" width="70" height="20" as="geometry"/></mxCell>')
        xml_parts.append('<mxCell id="layer2_label" value="Show AST Nodes" parent="0" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;" vertex="1"><mxGeometry x="35" y="35" width="100" height="20" as="geometry"/></mxCell>')
        xml_parts.append('<mxCell id="layer3_label" value="Show Field Details" parent="0" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;" vertex="1"><mxGeometry x="35" y="60" width="120" height="20" as="geometry"/></mxCell>')
        
        # Close XML structure
        xml_parts.append('</root>')
        xml_parts.append('</mxGraphModel>')
        xml_parts.append('</diagram>')
        xml_parts.append('</mxfile>')
        
        return '\n'.join(xml_parts)
    
    def _extract_field_content(self, value) -> str:
        """Extract readable content from AST field values"""
        if isinstance(value, ast.AST):
            node_type = type(value).__name__
            if hasattr(value, 'name'):
                return f"{node_type}: {value.name}"
            elif hasattr(value, 'id'):
                return f"{node_type}: {value.id}"
            elif hasattr(value, 'arg'):
                return f"{node_type}: {value.arg}"
            return node_type
        elif isinstance(value, list) and value:
            if isinstance(value[0], ast.AST):
                return f"[{type(value[0]).__name__}...]"
            else:
                return str(value)
        elif isinstance(value, str):
            return value
        elif hasattr(value, '__dict__'):
            if hasattr(value, 'name'):
                return f"name: {value.name}"
            elif hasattr(value, 'id'):
                return f"id: {value.id}"
            elif hasattr(value, 'arg'):
                return f"arg: {value.arg}"
        return str(value) if value is not None else ""
    
    def save_diagram(self, ast_tree: ast.AST):
        """Generate and save the Draw.io XML file"""
        time_now = datetime.now()
        filename = f"./data/vizualization/ast_diagram_{time_now.strftime('%Y-%m-%d_%H-%M-%S')}.drawio"
        
        xml_content = self.generate_diagram_xml(ast_tree)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        print(f"Interactive Draw.io diagram saved to: {filename}")
        print("Open in Draw.io and use the layer checkboxes in the bottom-left to show/hide different levels!")
        return filename