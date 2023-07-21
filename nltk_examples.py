import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Baixe os recursos necessários
nltk.download('stopwords')
nltk.download('wordnet')

# Exemplo de texto
text = "Os gatos estão pulando sobre as cercas e correndo nos jardins"

# Tokenização
tokens = nltk.word_tokenize(text)

# Remoção de stopwords
stop_words = set(stopwords.words('portuguese'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Lematização
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

# Resultados
print("Tokens originais:", tokens)
print("Tokens filtrados:", filtered_tokens)
print("Tokens lematizados:", lemmatized_tokens)