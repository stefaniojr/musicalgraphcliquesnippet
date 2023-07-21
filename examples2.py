import networkx as nx
import matplotlib.pyplot as plt

# Star Graph
def generate_star_graph(n):
    G = nx.star_graph(n)
    return G

# Cycle Graph
def generate_cycle_graph(n):
    G = nx.cycle_graph(n)
    return G

# Complete Graph
def generate_complete_graph(n):
    G = nx.complete_graph(n)
    return G

# Função para mapear números para letras
def map_node_labels(G):
    mapping = {i: chr(65 + i) for i in G.nodes()}
    G = nx.relabel_nodes(G, mapping)
    return G

# Example usage
n = 6

star_graph = generate_star_graph(n)
star_graph = map_node_labels(star_graph)
plt.figure()
nx.draw(star_graph, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')
plt.title("Grafo Estrela")
plt.savefig("grafo_estrela.png")  # Save as an image

cycle_graph = generate_cycle_graph(n)
cycle_graph = map_node_labels(cycle_graph)
plt.figure()
nx.draw(cycle_graph, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')
plt.title("Grafo Círculo")
plt.savefig("grafo_circulo.png")  # Save as an image

complete_graph = generate_complete_graph(n)
complete_graph = map_node_labels(complete_graph)
plt.figure()
nx.draw(complete_graph, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')
plt.title("Grafo Completo")
plt.savefig("grafo_completo.png")  # Save as an image