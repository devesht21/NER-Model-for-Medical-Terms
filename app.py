import spacy
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    text_en = request.form["entities"]
    nlp_ner = spacy.load("model-best")
    doc = nlp_ner(text_en)
    entities = []
    labels = []
    for ent in doc.ents:
        entities.append(ent.text)
        labels.append(ent.label_)
    final_list = []
    for e, l in list(zip(entities, labels)):
        final_list.append(e + " -> " + l)
    return render_template("predict.html", msg=text_en, text=final_list)


if __name__ == "__main__":
    app.run(debug=True)
