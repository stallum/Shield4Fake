import pickle


# Carregar modelo e vetorizador já treinados
with open('app/modelos/modelo_treinado_en.pkl', 'rb') as f:
    modelo = pickle.load(f)

with open('app/modelos/vetorizador.pkl', 'rb') as f:
    vetorizador = pickle.load(f)

# Função que recebe uma string e retorna o rótulo
def classificarNoticiaEn(texto: str):
    texto_vetor = vetorizador.transform([texto])
    label = modelo.predict(texto_vetor)[0]

    if label.upper() == 'TRUE':
        label = 'Real'
    else: 
        label = 'Fake'

    return label