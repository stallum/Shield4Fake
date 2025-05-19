import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv('data/pre-processed.csv')

X = df['preprocessed_news']
Y = df['label']

# vetorização de texto usado para treinar o modelo de Processamento de Linguagem Natural
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Criação do modelo 
X_train, X_test, y_train, y_test = train_test_split(X_vec, Y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# Salvar modelo e vetorizador
joblib.dump(model, 'app/models/fake_news_model.pkl')
joblib.dump(vectorizer, 'app/models/tfidf_vectorizer.pkl')

#atualizar novos modelos