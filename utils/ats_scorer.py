from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(resume_text, jd_text, matched_skills, jd_skills):
    """
    Returns ATS score as percentage (0–100)
    """

    # ---------- 1. Skill Match (50%) ----------
    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / len(jd_skills)) * 50

    # ---------- 2. Content Similarity (40%) ----------
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    similarity_score = similarity * 40

    # ---------- 3. Keyword Coverage (10%) ----------
    jd_words = set(jd_text.split())
    resume_words = set(resume_text.split())

    if len(jd_words) == 0:
        keyword_score = 0
    else:
        keyword_score = (len(jd_words & resume_words) / len(jd_words)) * 10

    total = skill_score + similarity_score + keyword_score

    return {
        "final_score": round(total, 2),
        "skill_score": round(skill_score, 2),
        "similarity_score": round(similarity_score, 2),
        "keyword_score": round(keyword_score, 2),
    }
