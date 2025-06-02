import pickle


# Carregar modelo e vetorizador já treinados
with open('app/modelos/modelo_rf_pt.pkl', 'rb') as f:
    modelo = pickle.load(f)

with open('app/modelos/vetorizador_tfidf_pt.pkl', 'rb') as f:
    vetorizador = pickle.load(f)

# Dicionário de rótulos
labels = ['Fake', 'Real']

# Função que recebe uma string e retorna o rótulo
def classificarNoticia(texto: str):
    texto_vetor = vetorizador.transform([texto])
    label = modelo.predict(texto_vetor)[0]

    if label.upper() == 'TRUE':
        label = 'Real'
    else: 
        label = 'Fake'

    return label