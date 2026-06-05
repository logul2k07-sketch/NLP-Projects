from flask import Flask, render_template, request, jsonify
from grammar_checker import check_grammar, correct_text, analyze_sentence, highlight_errors

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided"}), 400

    errors = check_grammar(text)
    corrected = correct_text(text) if errors else text
    highlighted = highlight_errors(text, errors)
    tokens = analyze_sentence(text)

    return jsonify({
        "errors": errors,
        "corrected": corrected,
        "highlighted": highlighted,
        "tokens": tokens,
        "error_count": len(errors),
    })


if __name__ == "__main__":
    app.run(debug=True, port=1001)
