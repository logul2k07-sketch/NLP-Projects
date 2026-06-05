import re
from collections import defaultdict

CATEGORIES = {
    "Politics": [
        "government", "president", "election", "senate", "congress", "parliament",
        "minister", "policy", "vote", "democrat", "republican", "political", "law",
        "legislation", "campaign", "diplomatic", "white house", "party", "governor"
    ],
    "Technology": [
        "ai", "artificial intelligence", "software", "hardware", "tech", "robot",
        "smartphone", "internet", "cyber", "data", "algorithm", "startup", "app",
        "machine learning", "cloud", "digital", "innovation", "computer", "coding", "5g"
    ],
    "Sports": [
        "football", "basketball", "soccer", "tennis", "cricket", "olympics",
        "championship", "tournament", "athlete", "stadium", "coach", "player",
        "team", "match", "score", "league", "goal", "winner", "medal", "sport"
    ],
    "Health": [
        "health", "medical", "hospital", "doctor", "vaccine", "disease", "cancer",
        "mental health", "surgery", "drug", "treatment", "patient", "virus", "pandemic",
        "nutrition", "exercise", "fitness", "wellness", "pharmacy", "symptom"
    ],
    "Business": [
        "market", "stock", "economy", "trade", "company", "startup", "investment",
        "finance", "bank", "revenue", "profit", "inflation", "gdp", "merger",
        "acquisition", "ceo", "corporation", "entrepreneur", "nasdaq", "business"
    ],
    "Entertainment": [
        "movie", "music", "celebrity", "actor", "actress", "film", "concert",
        "album", "award", "oscar", "grammy", "netflix", "tv show", "series",
        "box office", "streaming", "hollywood", "director", "fashion", "pop culture"
    ],
    "Science": [
        "research", "scientist", "discovery", "space", "nasa", "climate", "biology",
        "chemistry", "physics", "experiment", "fossil", "planet", "universe",
        "gene", "dna", "study", "laboratory", "environment", "species", "astronomy"
    ],
    "World": [
        "war", "conflict", "refugee", "united nations", "un", "nato", "treaty",
        "sanctions", "protest", "crisis", "international", "foreign", "embassy",
        "military", "troops", "invasion", "global", "aid", "humanitarian", "coup"
    ],
}


def preprocess(text):
    return re.sub(r"[^a-z0-9\s]", "", text.lower())


def classify(text):
    cleaned = preprocess(text)
    scores = defaultdict(int)

    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in cleaned:
                scores[category] += 1

    if not scores:
        return {"category": "Unknown", "confidence": 0, "scores": {}}

    total = sum(scores.values())
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_category, top_count = sorted_scores[0]
    confidence = round((top_count / total) * 100, 1)

    return {
        "category": top_category,
        "confidence": confidence,
        "scores": dict(sorted_scores),
    }
