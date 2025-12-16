def extract_skills(text, skill_list):
    found_skills = set()

    for skill in skill_list:
        if skill in text:
            found_skills.add(skill)

    return found_skills


if __name__ == "__main__":
    # sample resume text
    resume_text = """
    python developer with experience in flask and sql.
    worked on machine learning projects and git.
    """

    # sample job description text
    jd_text = """
    looking for a software engineer with python, django,
    sql, docker, and git experience.
    """

    skills = [
        "python", "java", "c", "c++", "sql", "flask", "django",
        "machine learning", "git", "docker", "aws", "react"
    ]

    resume_skills = extract_skills(resume_text, skills)
    jd_skills = extract_skills(jd_text, skills)

    matched_skills = resume_skills & jd_skills
    missing_skills = jd_skills - resume_skills

    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)
    print("Matched Skills:", matched_skills)
    print("Missing Skills:", missing_skills)
