from deep_translator import GoogleTranslator

def traducao(texto, source='pt', target='en'):
    try:
        return GoogleTranslator(source=source, target=target).translate(texto)
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return texto

