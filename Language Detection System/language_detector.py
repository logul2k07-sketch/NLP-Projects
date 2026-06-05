from langdetect import detect, detect_langs, LangDetectException
import pycountry

def get_language_name(code):
    try:
        lang = pycountry.languages.get(alpha_2=code)
        return lang.name if lang else code.upper()
    except:
        return code.upper()

def detect_language(text):
    try:
        lang_code = detect(text)
        probabilities = detect_langs(text)
        lang_name = get_language_name(lang_code)
        top_langs = [
            {"language": get_language_name(str(l).split(":")[0]), "confidence": round(float(str(l).split(":")[1]) * 100, 2)}
            for l in probabilities[:3]
        ]
        return {
            "detected_language": lang_name,
            "language_code": lang_code,
            "confidence": top_langs[0]["confidence"] if top_langs else 0,
            "top_languages": top_langs
        }
    except LangDetectException:
        return {"error": "Could not detect language. Please provide more text."}
