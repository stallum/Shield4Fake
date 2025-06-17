from flask import Flask, render_template, request
from scripts.modelo_pt import classificarNoticiaPt
from scripts.modelo_en import classificarNoticiaEn
from scripts.spider import extrairTexto

app = Flask(__name__)

# rota de home do projeto
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    
    if request.method == 'POST':
        
        if 'link' in request.form.get('link', ''):
            url = request.form['link']
            noticia = extrairTexto(url)
        elif 'noticia' in request.form.get('noticia', '').strip():
            noticia = request.form['noticia']
        else: 
            noticia = ''
        

        # Coleta o idioma (padrão = pt)
        idioma = request.form.get('idioma', 'pt')

        # Chama o classificador certo
        if noticia == '':
            label = '❗Não há uma noticia inserida'
        elif idioma == 'pt':
            label = classificarNoticiaPt(str(noticia))
        else:
            label = classificarNoticiaEn(str(noticia))

        resultado = {
            # Classificação
            'label': f'🔎{label}',
            'noticia' :  f'{noticia}'
        }
    return render_template('teste.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)