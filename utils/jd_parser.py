import re

def clean_text(text):
    # convert to lowercase
    text = text.lower()

    # remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def parse_job_description(jd_text):
    return clean_text(jd_text)


if __name__ == "__main__":
    job_description = """
    We are looking for a Software Engineer with strong Python skills.
    Experience with Flask, REST APIs, SQL, and Git is required.
    Knowledge of machine learning is a plus.
    """

    cleaned_jd = parse_job_description(job_description)
    print(cleaned_jd)
