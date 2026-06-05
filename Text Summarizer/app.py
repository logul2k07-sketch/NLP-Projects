from flask import Flask, render_template, request, jsonify
from summarizer import summarize

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.get_json()
    text = data.get("text", "").strip()
    num_sentences = int(data.get("num_sentences", 3))
    if not text:
        return jsonify({"error": "Text is required."}), 400
    summary = summarize(text, num_sentences)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(port=1005, debug=True)
