from dataclasses import dataclass
from datetime import datetime
from pyvis.network import Network
from pathlib import Path
# @dataclass
# class Visualizer:
#     conf: Network 
#     file_content: str
#     file_name:Path
#     @property
#     def net(self) -> Network:
#         self.conf.add_node(
#             "Root", 
#             label=f"<b>FILE: {self.file_name}</b>\n<i>--------------------</i>\n{self.file_content}",
#             shape="box",
#             color={
#                 "background": "#2b2b2b", # Dark theme 'Body'
#                 "border": "#00ff00",     # Neon green border
#             },
#             font={
#                 "color": "white", 
#                 "face": "monospace", 
#                 "align": "left",
#                 "multi": "html"
#             },
#             borderWidth=2,
#             margin=15
#         )
#         return self.conf
#     @staticmethod # i used static because i don't need any implicit usage of instance parameter instead of using class methode, in other word it doen't belong to a particular instance
#     def generate_graph(net: Network):
#         net.toggle_physics(True)
#         time_now = datetime.now()
#         net.save_graph(f"./data/vizualization/vizualization_{time_now}.html")
#         with open(f"./data/vizualization/vizualization_{time_now}.html","a") as f:
#             javascript_logic = """
#             network.on("click", function (params) {
#                 if (params.nodes.length > 0) {
#                     var parentId = params.nodes[0];
                    
#                     // FIX: Only get 'to' nodes (children). 
#                     // This prevents the script from finding and hiding the parent/root node.
#                     var childIds = network.getConnectedNodes(parentId, 'to');
                    
#                     if (childIds.length > 0) {
#                         // Check the current state of the first child
#                         var firstChild = nodes.get(childIds[0]);
#                         var shouldHide = !firstChild.hidden;
                        
#                         var updates = [];
#                         for (var i = 0; i < childIds.length; i++) {
#                             updates.push({
#                                 id: childIds[i], 
#                                 hidden: shouldHide
#                             });
#                         }
#                         nodes.update(updates);
#                     }
#                 }
#             });""";
#             f.write(f"<script>{javascript_logic}</script>")


@dataclass
class Visualizer:
    conf: Network 
    file_content: str
    file_name: Path
    
    @property
    def net(self) -> Network:
        # Store file content for JavaScript access (escaped for safety)
        self.conf.add_node(
            "Root", 
            label=f"<b>FILE: {self.file_name.name}</b><br><i>(Hover to see content)</i>",
            shape="box",
            color={
                "background": "#2b2b2b",
                "border": "#00ff00",
            },
            font={
                "color": "white", 
                "face": "monospace", 
                "align": "center",
                "multi": "html"
            },
            borderWidth=2,
            margin=15,
            title="",  # Will be set dynamically
        )
        return self.conf
    
    @staticmethod
    def generate_graph(net: Network):
        time_now = datetime.now()
        filename = f"./data/vizualization/vizualization_{time_now}.html"
        net.save_graph(filename)
        
        # Read the saved file to get the file content (we'll pass it via a different method)
        # For now, we'll inject the content directly into the JavaScript
        
        with open(filename, "a") as f:
            # Get file content from the network data (this is a bit hacky but works)
            # We'll assume the visualizer instance has access to the content
            
            javascript_logic = """
            <script>
            // Enhanced hover functionality for root node
            var originalLabel = '';
            var fileContent = `{file_content}`;  // This will be injected
            
            network.on("hoverNode", function (params) {{
                var nodeId = params.node;
                if (nodeId === "Root") {{
                    var node = nodes.get(nodeId);
                    originalLabel = node.label;
                    
                    // Create a formatted content preview with scrollable area
                    var contentPreview = fileContent.length > 300 
                        ? fileContent.substring(0, 300) + "...\\n\\n<i>(Click to expand)</i>"
                        : fileContent;
                    
                    var hoverLabel = `<b>FILE: {file_name}</b>\\n<i>--------------------</i>\\n` + 
                                   `<div style="max-height: 250px; overflow-y: auto; font-size: 10px; white-space: pre-wrap; background: #1a1a1a; padding: 5px; border-radius: 3px;">` + 
                                   contentPreview.replace(/</g, '&lt;').replace(/>/g, '&gt;') + 
                                   `</div>`;
                    
                    nodes.update({{id: nodeId, label: hoverLabel}});
                    
                    // Highlight the node on hover
                    network.selectNodes([nodeId]);
                }}
            }});
            
            network.on("blurNode", function (params) {{
                var nodeId = params.node;
                if (nodeId === "Root" && originalLabel) {{
                    nodes.update({{id: nodeId, label: originalLabel}});
                    network.unselectAll();
                }}
            }});
            
            // Enhanced click functionality
            network.on("click", function (params) {{
                if (params.nodes.length > 0) {{
                    var nodeId = params.nodes[0];
                    
                    if (nodeId === "Root") {{
                        // Toggle full content view for Root node
                        var node = nodes.get(nodeId);
                        var isExpanded = node.label.includes("...(Click to expand)");
                        
                        if (isExpanded) {{
                            var fullContent = `<b>FILE: {file_name}</b>\\n<i>--------------------</i>\\n` + 
                                            `<div style="max-height: 400px; overflow-y: auto; font-size: 10px; white-space: pre-wrap; background: #1a1a1a; padding: 8px; border-radius: 5px; border: 1px solid #00ff00;">` + 
                                            fileContent.replace(/</g, '&lt;').replace(/>/g, '&gt;') + 
                                            `</div>`;
                            nodes.update({{id: nodeId, label: fullContent}});
                        }}
                        return;
                    }}
                    
                    // Original click logic for other nodes
                    var childIds = network.getConnectedNodes(nodeId, 'to');
                    
                    if (childIds.length > 0) {{
                        var firstChild = nodes.get(childIds[0]);
                        var shouldHide = !firstChild.hidden;
                        
                        var updates = [];
                        for (var i = 0; i < childIds.length; i++) {{
                            updates.push({{
                                id: childIds[i], 
                                hidden: shouldHide
                            }});
                        }}
                        nodes.update(updates);
                    }}
                }}
            }});
            </script>
            """
            
            # We need to inject the actual file content and filename
            # Since this is a static method, we'll need to modify the approach
            # For now, let's create an instance method instead
            
            f.write(javascript_logic)