import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_md")


def preprocess(text):
    doc = nlp(text.lower())
    return " ".join(token.lemma_ for token in doc if not token.is_stop and not token.is_punct)


def spacy_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return round(doc1.similarity(doc2) * 100, 2)


def tfidf_similarity(text1, text2):
    p1, p2 = preprocess(text1), preprocess(text2)
    vectors = TfidfVectorizer().fit_transform([p1, p2])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)


def get_similarity_label(score):
    if score >= 80:
        return "Very Similar [HIGH]"
    elif score >= 50:
        return "Moderately Similar [MED]"
    elif score >= 25:
        return "Slightly Similar [LOW]"
    else:
        return "Not Similar [NONE]"


def check_similarity(text1, text2):
    spacy_score = spacy_similarity(text1, text2)
    tfidf_score = tfidf_similarity(text1, text2)
    avg_score = round((spacy_score + tfidf_score) / 2, 2)
    return {
        "spacy": spacy_score,
        "tfidf": tfidf_score,
        "average": avg_score,
        "label": get_similarity_label(avg_score),
    }
