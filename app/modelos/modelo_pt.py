import pandas as pd
from sklearn.preprocessing import LabelEncoder 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from data.data import dataset

dfPt = pd.read_csv('app/modelos/data/data.csv')

tokenizacao = LabelEncoder()
dfPt['label'] = tokenizacao.fit_transform(dfPt['label'])
dfPt.head()

dfPt.to_csv('app/modelos/data/data-clean.csv', index=False)

dfPt = pd.read_csv('app/modelos/data/data-clean.csv')

x = dfPt['preprocessed_news']

y = dfPt['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier()
vetorizador = TfidfVectorizer()

x_train = vetorizador.fit_transform(x_train)
x_test = vetorizador.transform(x_test)
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)
acuracia = accuracy_score(y_test, y_pred)
print(f'{acuracia:.2f}')
def classificarNoticiaPt(texto):
    label = modelo.predict(vetorizador.transform([texto]))
    confianca = accuracy_score(y_test, y_pred)

    labels = ['Fake', 'Real']
    return label, confianca