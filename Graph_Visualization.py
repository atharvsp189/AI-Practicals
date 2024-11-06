import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")

# Position the nodes
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=5000, edge_color='gray')

# Show the plot
plt.show()

