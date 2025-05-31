from flask import Flask, render_template, request
from scripts.modelo import classificarNoticia
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    
    if request.method == 'POST':
        noticia = request.form['noticia']
        label = classificarNoticia(noticia)
        resultado = {
            # Classificação
            'label': f'🔎{label.upper()}'
            # 'noticia': f'{noticia}',
            # 'noticia_traduzida': f'{noticia_traduzida}'
        }
    return render_template('teste.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)