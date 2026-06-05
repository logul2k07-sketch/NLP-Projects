from flask import Flask, render_template, request, jsonify
from classifier import classify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/classify", methods=["POST"])
def classify_news():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "News text is required."}), 400
    result = classify(text)
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=1006, debug=True)
