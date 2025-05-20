from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# não coloquei o nome em português porque fica muito feio.
modelName = "Pulk17/Fake-News-Detection"
tokenizer = AutoTokenizer.from_pretrained(modelName)
modelo = AutoModelForSequenceClassification.from_pretrained(modelName)

# Função para classificar a noticia
def classificarNoticia(texto): 
    """
    essa função classifica a noticia entre "Real" e "Fake" utilziando o processo de tokenização da notícia inserida em um input e processada pelo modelo de Processamento de Linguagem Natural.
    """
    inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = modelo(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1)
        predicted_class = int(torch.argmax(probs, dim=1).item())
        confidence = probs[0][predicted_class].item()

        labels = ['Fake', 'Real']
        return labels[predicted_class], confidence

user_input = input("Digite a notícia para classificar: ")

# Classificação
label, confidence = classificarNoticia(user_input)
print(f"\n🔎 Resultado: {label}")
print(f"📊 Confiança: ({confidence*100:.2f}% de confiança)")