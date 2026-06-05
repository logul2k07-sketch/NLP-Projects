from flask import Flask, render_template, request, jsonify
from similarity_checker import check_similarity

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    text1 = data.get("text1", "").strip()
    text2 = data.get("text2", "").strip()
    if not text1 or not text2:
        return jsonify({"error": "Both texts are required."}), 400
    result = check_similarity(text1, text2)
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=1003, debug=True)
