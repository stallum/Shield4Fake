from flask import Flask, render_template, request
from scripts.modelo import classificarNoticia
from langdetect import detect
from scripts.traducao import traducao

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    noticia_traduzida = None
    
    if request.method == 'POST':
        noticia = request.form['noticia']
        idioma = detect(noticia)
        if idioma == 'pt':
            noticia_traduzida = traducao(noticia)
        else: 
            noticia_traduzida = noticia                 
                   
        label, confianca = classificarNoticia(noticia_traduzida)
        resultado = {
            # Classificação
            'label': f'🔎 Resultado: {label}',
            'confianca': f'📊 Confiança: ({confianca*100:.2f}% de confiança)',
            'noticia': f'{noticia}',
            'noticia_traduzida': f'{noticia_traduzida}'
        }
    return render_template('teste.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)