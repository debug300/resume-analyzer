from flask import Flask, render_template, request
import os

from utils.resume_parser import extract_text_from_pdf
from utils.jd_parser import parse_job_description
from utils.skill_extractor import extract_skills
from utils.ats_scorer import calculate_ats_score

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

SKILLS = [
    "python", "java", "c", "c++", "sql", "flask", "django",
    "machine learning", "git", "docker", "aws", "react"
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        resume = request.files["resume"]
        jd_text = request.form["jd"]

        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
        resume.save(resume_path)

        resume_text = extract_text_from_pdf(resume_path)
        jd_clean = parse_job_description(jd_text)

        resume_skills = extract_skills(resume_text, SKILLS)
        jd_skills = extract_skills(jd_clean, SKILLS)

        matched_skills = resume_skills & jd_skills
        missing_skills = jd_skills - resume_skills

        ats_score = calculate_ats_score(resume_text, jd_clean)

        result = {
            "score": ats_score,
            "matched": matched_skills,
            "missing": missing_skills
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
