from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CORE_SKILLS = ["java", "spring boot", "sql"]
IMPORTANT_SKILLS = ["git", "docker", "aws"]
OPTIONAL_SKILLS = ["kubernetes", "microservices", "ci cd"]


def calculate_ats_score(resume_text, jd_text, matched_skills, jd_skills):
    # ---------- Skill Group Scoring ----------
    def score_group(skills, weight):
        if not skills:
            return 0
        matched = set(skills) & matched_skills
        return (len(matched) / len(skills)) * weight

    core_score = score_group(CORE_SKILLS, 40)
    important_score = score_group(IMPORTANT_SKILLS, 20)
    optional_score = score_group(OPTIONAL_SKILLS, 10)

    skill_score = core_score + important_score + optional_score  # max 70

    # ---------- Content Similarity ----------
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    similarity_score = similarity * 20

    # ---------- Keyword Coverage ----------
    jd_words = set(jd_text.split())
    resume_words = set(resume_text.split())
    keyword_score = (len(jd_words & resume_words) / len(jd_words)) * 10 if jd_words else 0

    # ---------- Final Score ----------
    total_score = skill_score + similarity_score + keyword_score

    # Realism floor
    if core_score >= 20:
        total_score = max(total_score, 60)

    # ---------- Explanation ----------
    reasons = []
    suggestions = []

    missing_core = set(CORE_SKILLS) - matched_skills
    missing_important = set(IMPORTANT_SKILLS) - matched_skills

    if missing_core:
        reasons.append(f"Missing core skills: {', '.join(missing_core)}")
        for s in missing_core:
            suggestions.append(f"Add a project or experience mentioning {s}")

    if missing_important:
        reasons.append(f"Missing important skills: {', '.join(missing_important)}")
        for s in missing_important:
            suggestions.append(f"Include hands-on usage of {s}")

    if similarity_score < 8:
        reasons.append("Low resume and job description similarity")
        suggestions.append("Rewrite experience using job description terminology")

    if keyword_score < 4:
        reasons.append("Low keyword coverage")
        suggestions.append("Add more job-related keywords naturally")

    if not reasons:
        reasons.append("Resume aligns well with job description")

    return {
        "final_score": round(min(total_score, 100), 2),
        "skill_score": round(skill_score, 2),
        "similarity_score": round(similarity_score, 2),
        "keyword_score": round(keyword_score, 2),
        "reasons": reasons,
        "suggestions": suggestions
    }
