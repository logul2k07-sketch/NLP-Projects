import spacy
import language_tool_python

nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool("en-US")


def analyze_sentence(text):
    doc = nlp(text)
    tokens = [(token.text, token.pos_, token.dep_) for token in doc]
    return tokens


def check_grammar(text):
    matches = tool.check(text)
    errors = []
    for match in matches:
        errors.append({
            "message": match.message,
            "suggestions": match.replacements[:3],
            "offset": match.offset,
            "length": match.error_length,
            "context": match.context,
        })
    return errors


def correct_text(text):
    return language_tool_python.utils.correct(text, tool.check(text))


def highlight_errors(text, errors):
    if not errors:
        return text
    result = list(text)
    for error in sorted(errors, key=lambda e: e["offset"], reverse=True):
        start = error["offset"]
        end = start + error["length"]
        result.insert(end, "]")
        result.insert(start, "[")
    return "".join(result)
