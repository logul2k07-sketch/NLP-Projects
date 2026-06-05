from flask import Flask, render_template, request, jsonify
from language_detector import detect_language

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "Text is required."}), 400
    result = detect_language(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=1004, debug=True)
