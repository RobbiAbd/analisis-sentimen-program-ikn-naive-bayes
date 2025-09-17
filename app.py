from flask import Flask, request, jsonify, render_template
import pickle
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import pandas as pd

app = Flask(__name__)

with open('./model/naive_bayes_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('./model/count_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def preprocess(text: str) -> str:
    if not isinstance(text, str):
        return ''
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+|\@\w+|\#|[^a-zA-Z\s]', ' ', text)
    words = text.split()
    return ' '.join(words)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get("komentar")
    processed = preprocess(data)
    vec = vectorizer.transform([processed])
    pred = model.predict(vec)[0]
    return jsonify({"komentar": data, "sentimen": pred})

@app.route("/data")
def data():
    df = pd.read_csv("data/preprocessed_data.csv")
    df['label'] = df['label'].astype(str).apply(lambda x: x.split('/')[0])
    counts = df['label'].value_counts().to_dict()
    return jsonify(counts)

if __name__ == "__main__":
    app.run(debug=True)
