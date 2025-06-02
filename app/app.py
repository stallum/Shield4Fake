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
            'label': f'🔎{label}'
        }
    return render_template('teste.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)