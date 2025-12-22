from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text, jd_text, matched_skills, jd_skills):
    # ---------- TEXT SIMILARITY (25%) ----------
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    text_similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100

    # ---------- SKILL MATCH (75%) ----------
    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / len(jd_skills)) * 100

    # ---------- FINAL ATS ----------
    final_score = max(
        (0.75 * skill_score) + (0.25 * text_similarity),
        skill_score * 0.9
    )

    return round(final_score, 2)
