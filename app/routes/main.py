from flask import Blueprint, request, render_template
import joblib

routes = Blueprint('routes', __name__)

model = joblib.load("app/model/fake_news_model.pkl")
vectorizer = joblib.load("app/model/tfidf_vectorizer.pkl")

@routes.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        text = request.form['text']
        vec = vectorizer.transform([text])
        pred = model.predict(vec)[0]
        prediction = 'Fake' if pred == 1 else 'Real'
    return render_template('index.html', prediction=prediction)
