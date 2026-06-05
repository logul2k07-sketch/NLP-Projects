import spacy
from collections import Counter
import re

nlp = spacy.load("en_core_web_sm")

STOP_WORDS = nlp.Defaults.stop_words

def extract_keywords(text, top_n=10):
    text = re.sub(r'\s+', ' ', text.strip())
    doc = nlp(text)

    keywords = []
    for token in doc:
        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
            and token.pos_ in ("NOUN", "PROPN", "VERB", "ADJ")
            and len(token.lemma_) > 2
        ):
            keywords.append(token.lemma_.lower())

    freq = Counter(keywords)
    total = sum(freq.values()) or 1

    results = [
        {
            "keyword": word,
            "count": count,
            "score": round(count / total * 100, 2)
        }
        for word, count in freq.most_common(top_n)
    ]
    return results


def extract_noun_phrases(text):
    doc = nlp(text)
    return list({chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text) > 2})


def get_named_entities(text):
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
