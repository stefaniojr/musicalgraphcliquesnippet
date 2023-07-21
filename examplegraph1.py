import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo vazio
G = nx.Graph()

# Adicionando nós
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Adicionando arestas
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Desenha o grafo
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=1000, font_size=12, font_weight='bold')

# Salva a figura como PNG
plt.savefig('grafo_example1.png', format='png')
