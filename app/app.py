from flask import Flask, render_template, request
from scripts.modelo import classificarNoticia
from scripts.scrapy import extrairTexto

app = Flask(__name__)

# rota de home do projeto
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    
    if request.method == 'POST':
        if 'noticia' in request.form:
            noticia = request.form['noticia']
        else:
            if 'link' in request.form:
                url = request.form['link']
                noticia = extrairTexto(url)
        
        label = classificarNoticia(str(noticia))
        resultado = {
            # Classificação
            'label': f'🔎{label}'
        }
    return render_template('teste.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)