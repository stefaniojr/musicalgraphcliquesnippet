import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image

# Cria o grafo
G = nx.Graph()

# Adiciona os nós
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)

# Adiciona as arestas
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'),
         ('F', 'A'), ('A', 'C'), ('B', 'D'), ('D', 'F')]
G.add_edges_from(edges)


max_cliques = list(nx.find_cliques(G)) # max cliques
all_cliques = list(nx.find_cliques(G)) # all cliques

# Desenha o grafo
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=1000, font_size=12, font_weight='bold')

# Salva a figura como PNG
plt.savefig('grafo.png', format='png')

images = []

for i, clique in enumerate(max_cliques):

    # Cria uma cópia do grafo original
    H = G.copy()
    # Remove as arestas que não estão entre os vértices da clique atual
    H.remove_edges_from([(u, v) for u, v in H.edges() if u not in clique or v not in clique])

    pos = nx.circular_layout(G)
    node_colors = ['red' if node in clique else 'lightblue' for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors,
            node_size=1000, font_size=12, font_weight='bold')
    filename = f"clique_{i+1}.png"

    plt.savefig(filename, format='png')
    plt.gcf()
 
    # Adiciona a imagem à lista
    images.append(Image.open(filename))

# Calcula o tamanho da imagem final
num_images = len(images)
num_rows = (num_images + 2) // 3  # Divide o número de imagens em 3 colunas
width, height = images[0].size
final_width = width * 2
final_height = height * num_rows

# Cria a imagem final
final_image = Image.new('RGB', (final_width, final_height))

# Combina as imagens em uma única imagem
x_offset = 0
y_offset = 0
for img in images:
    final_image.paste(img, (x_offset, y_offset))

    x_offset += width
    if x_offset == final_width:
        x_offset = 0
        y_offset += height

# Salva a imagem final
final_image.save('cliques.png')

print("Imagem final salva.")