import ast
from dataclasses import dataclass
from datetime import datetime
from pyvis.network import Network

@dataclass
class Visualizer:
    conf: Network 
    @property
    def net(self) -> Network:
        self.conf.add_node(
            "Root", 
            label=f"<b>FILE: test1.py</b>\n<i>--------------------</i>",
            shape="box",
            color={
                "background": "#2b2b2b", # Dark theme 'Body'
                "border": "#00ff00",     # Neon green border
            },
            font={
                "color": "white", 
                "face": "monospace", 
                "align": "left",
                "multi": "html"
            },
            borderWidth=2,
            margin=15
        )
        return self.conf
    @staticmethod # i used static because i don't need any implicit usage of instance parameter instead of using class methode, in other word it doen't belong to a particular instance
    def generate_graph(net: Network):
        net.toggle_physics(True)
        time_now = datetime.now()
        net.save_graph(f"./data/vizualization/vizualization_{time_now}.html")
        with open(f"./data/vizualization/vizualization_{time_now}.html","a") as f:
            javascript_logic = """
            network.on("click", function (params) {
                if (params.nodes.length > 0) {
                    var parentId = params.nodes[0];
                    
                    // FIX: Only get 'to' nodes (children). 
                    // This prevents the script from finding and hiding the parent/root node.
                    var childIds = network.getConnectedNodes(parentId, 'to');
                    
                    if (childIds.length > 0) {
                        // Check the current state of the first child
                        var firstChild = nodes.get(childIds[0]);
                        var shouldHide = !firstChild.hidden;
                        
                        var updates = [];
                        for (var i = 0; i < childIds.length; i++) {
                            updates.push({
                                id: childIds[i], 
                                hidden: shouldHide
                            });
                        }
                        nodes.update(updates);
                    }
                }
            });""";
            f.write(f"<script>{javascript_logic}</script>")


visualizer = Visualizer(conf=Network(height='600px', width='100%',directed=False, notebook=True, neighborhood_highlight=False, select_menu=False, filter_menu=False, bgcolor='#ffffff', font_color=False, layout=None, heading='', cdn_resources='local'))