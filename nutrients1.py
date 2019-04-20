import networkx as nx

G = nx.Graph([("A", "eggs"),])
G.add_node("spinach") #add a single node
G.add_node("Hg") #add a single node by mistake
G.add_nodes_from(["folates", "asparagus", "liver"]) #Add a list of nodes
G.add_edge("spinach", "folates") # Add one edge, both ends exist
G.add_edge("spinach", "heating oil") # Add one edge by mistake
G.add_edge("liver", "Se") # Add one edge, one end does not exist
G.add_edges_from([("folates", "liver"), ("folates", "asparagus")])

G.remove_node("Hg")
G.remove_nodes_from(["Hg"])
