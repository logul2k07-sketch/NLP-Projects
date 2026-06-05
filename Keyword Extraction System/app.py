from flask import Flask, render_template, request, jsonify
from keyword_extractor import extract_keywords, extract_noun_phrases, get_named_entities

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract():
    data = request.get_json()
    text = data.get("text", "").strip()
    top_n = int(data.get("top_n", 10))

    if not text:
        return jsonify({"error": "No text provided"}), 400

    keywords = extract_keywords(text, top_n)
    noun_phrases = extract_noun_phrases(text)
    entities = get_named_entities(text)

    return jsonify({
        "keywords": keywords,
        "noun_phrases": noun_phrases[:10],
        "entities": entities
    })

if __name__ == "__main__":
    app.run(debug=True, port=1002)
