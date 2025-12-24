import os
from flask import Flask, render_template, request

from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_scorer import calculate_ats_score
from utils.text_cleaner import clean_text

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

SKILLS = [
    "python", "java", "sql", "spring boot", "rest api",
    "git", "docker", "aws",
    "kubernetes", "microservices",
    "data structures", "algorithms"
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        jd_text = request.form.get("jd", "")

        if not resume_file or resume_file.filename == "":
            return render_template("index.html", error="Please upload a resume")

        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
        resume_file.save(resume_path)

        resume_text = clean_text(extract_text_from_pdf(resume_path))
        jd_clean = clean_text(jd_text)

        resume_skills = extract_skills(resume_text, SKILLS)
        jd_skills = extract_skills(jd_clean, SKILLS)

        matched = resume_skills & jd_skills
        missing = jd_skills - resume_skills

        ats = calculate_ats_score(resume_text, jd_clean, matched, jd_skills)

        return render_template(
            "index.html",
            score=ats["final_score"],
            skill_score=ats["skill_score"],
            similarity_score=ats["similarity_score"],
            keyword_score=ats["keyword_score"],
            matched=matched,
            missing=missing,
            reasons=ats["reasons"],
            suggestions=ats["suggestions"]
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
