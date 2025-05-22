from flask import Flask, render_template, request
from scripts.modelo import classificarNoticia
from langdetect import detect
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    noticia_traduzida = None
    
    if request.method == 'POST':
        noticia = request.form['noticia']
        idioma = detect(noticia)
        if idioma != 'en':
            noticia_traduzida = GoogleTranslator(source='auto', target='en').translate(noticia)
        else: 
            noticia_traduzida = noticia 
                   
        label, confianca = classificarNoticia(noticia)
        resultado = {
            # Classificação
            'label': f'🔎 Resultado: {label}',
            'confianca': f"📊 Confiança: ({confianca*100:.2f}% de confiança)"
        }
    return render_template('teste.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)