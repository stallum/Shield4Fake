from flask import Flask, render_template, request
from scripts.modelo_pt import classificarNoticiaPt
from scripts.modelo_en import classificarNoticiaEn
from scripts.spider import organizarTexto

app = Flask(__name__)

# rota de home do projeto
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    
    if request.method == 'POST':
        
        link_input = request.form.get('link', '').strip()
        noticia_input = request.form.get('noticia', '').strip()

        if link_input:
            noticia = organizarTexto(link_input)
        elif noticia_input:
            noticia = noticia_input
        else:
            noticia = ''
        

        # Coleta o idioma (padrão = pt)
        idioma = request.form.get('idioma', 'pt')

        # Chama o classificador certo
        if noticia == ' ':
            label = '❗Não há uma noticia inserida'
        elif noticia == 'não foi possível extrair o texto desse link, porfavor copie todos os titulos, subtitulos e textos da notícia e copie na caixa acima':
            label = noticia
            noticia = ' '
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