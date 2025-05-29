from flask import Flask, render_template, request
from modelos.modelo_en import classificarNoticiaEn
from modelos.modelo_pt import classificarNoticiaPt
from langdetect import detect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    noticia_traduzida = None
    
    if request.method == 'POST':
        noticia = request.form['noticia']
        idioma = detect(noticia)
        if idioma == 'en':
            label, confianca = classificarNoticiaEn(noticia)
            resultado = {
                # Classificação
                'label': f'🔎 Resultado: {label}',
                'confianca': f'📊 Confiança: ({confianca*100:.2f}% de confiança)',
                'noticia': f'{noticia}',
                'noticia_traduzida': f'{noticia_traduzida}'
            }
        else: 
            label, confianca = classificarNoticiaPt(noticia)
            resultado = {
                # Classificação
                'label': f'🔎 Resultado: {label}',
                'confianca': f'📊 Confiança: ({confianca*100:.2f}% de confiança)',
                'noticia': f'{noticia}',
                'noticia_traduzida': f'{noticia_traduzida}' 
            }                
        
        # aplicar dropdrown na página
    return render_template('teste.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)