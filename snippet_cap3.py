from lyricsgenius import Genius
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import networkx as nx
import matplotlib.pyplot as plt
import random


def convert_to_lower_case(words):
    return [word.lower() for word in words]


def remove_punctuation(words):
    translator = str.maketrans('', '', string.punctuation)
    return [word.translate(translator) for word in words]


def remove_stopwords(words):
    stop_words = set(stopwords.words('english'))

    all_lyrics_no_stopwords = []
    for word in words:
        tokens = word_tokenize(word)
        lyrics_no_stopwords = [
            word for word in tokens if word not in stop_words]
        all_lyrics_no_stopwords.append(' '.join(lyrics_no_stopwords))

    return all_lyrics_no_stopwords


def execute_lemmatization(words):
    lemmatizer = WordNetLemmatizer()

    all_lyrics_lemmatized = []
    for lyrics in words:
        tokens = word_tokenize(lyrics)
        lyrics_lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
        all_lyrics_lemmatized.append(' '.join(lyrics_lemmatized))

    return all_lyrics_lemmatized

def remove_numbers(word):
    return re.sub(r'\d+', '', word)

def remove_numbers_words(text):
    words = text.split()
    words_without_number = [remove_numbers(word) for word in words]
    return ' '.join(words_without_number)


genius = Genius('HpJ0pnH7fP-sc9GodGLYDnXKn6lg7StqlYBZGggTCuP6k0ap9Q4-53_Vo88Rw221', remove_section_headers=True)

song = genius.search_song("All Too Well", "Taylor Swift")
lyrics_lines = song.lyrics.split("\n")
cleaned_lyrics_lines = lyrics_lines[1:-1] + [lyrics_lines[-1].replace("Embed", "").strip()]
cleaned_lyrics = "\n".join(cleaned_lyrics_lines)

for line in lyrics_lines[1:]:
    cleaned_words = [re.sub(r'\d+', '', word) for word in line.split()]
    cleaned_line = ' '.join(cleaned_words)
    cleaned_lyrics_lines.append(cleaned_line)


lyrics = remove_numbers_words(cleaned_lyrics)
lyrics = lyrics.split()

print(lyrics)

print('PONCTUATION')
lyrics = remove_punctuation(lyrics)
print(lyrics)

print('LOWERCASE')
lyrics = convert_to_lower_case(lyrics)
print(lyrics)

print('LEMATIZATION')
lyrics = execute_lemmatization(lyrics)
print(lyrics)

lyrics = remove_stopwords(lyrics)
lyrics = list(filter(lambda x: x != '', lyrics))
print('STOPWORDS')
print(lyrics)


def load_correlation_graph(words, context):
    graph = nx.Graph()

    # Percorre todas as palavras
    for i in range(len(words)):
        word = words[i]

        # Adicione o nó ao grafo se ainda não existir
        if word not in graph:
            graph.add_node(word)

        # Verifique as palavras vizinhas dentro de um contexto definido
        neighbors = words[max(0, i - context):i] + words[i+1:i+context+1]

        # Adicione as arestas entre a palavra atual e suas palavras vizinhas
        for neighbor in neighbors:
            if neighbor not in graph:
                graph.add_node(neighbor)
            graph.add_edge(word, neighbor)

    return graph

graph = load_correlation_graph(lyrics, 3)

# Layout do grafo
pos = nx.spring_layout(graph)

# Desenhe o grafo
nx.draw(graph, pos, with_labels=True, node_size=100, font_size=3, width=0.2)

# Salve a imagem como PNG
plt.savefig("graph.png", format="PNG", dpi=600)

plt.clf()

cliques = list(nx.find_cliques(graph))

print(cliques)

random_clique = random.choice(cliques)

# Crie uma cópia do layout antes de destacar a clique
pos_clique_highlight = pos.copy()

# Desenhe o grafo com as arestas e vértices da clique destacados em vermelho
nx.draw(graph, pos_clique_highlight, with_labels=True, node_size=100, font_size=3, width=0.2)

# Destaque os vértices da clique em vermelho
nx.draw_networkx_nodes(graph, pos_clique_highlight, nodelist=random_clique, node_color='red', node_size=100)

# Salve a imagem como PNG
plt.savefig("graph_with_highlighted_clique.png", format="PNG", dpi=600)


