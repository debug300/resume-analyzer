# AI-Powered ATS Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions using **Applicant Tracking System (ATS)** principles.  
The tool evaluates resume-job fit, explains score deductions, and provides actionable improvement suggestions.

---

## 🚀 Features

- 📄 Upload resume (PDF)
- 📝 Paste job description
- 📊 Realistic ATS score (0–100%)
- ⚖️ Skill importance weighting (Core / Important / Optional)
- 🔍 Resume–JD semantic similarity using NLP
- ❓ Explanation of why points were deducted
- ✅ Personalized resume improvement suggestions
- 🌐 Fully deployed web application

---

## 🧠 How ATS Scoring Works

The ATS score is calculated using a weighted approach similar to real-world systems:

| Component | Weight |
|---------|--------|
| Core Skills Match | 40% |
| Important Skills Match | 20% |
| Optional Skills Match | 10% |
| Content Similarity (TF-IDF + Cosine Similarity) | 20% |
| Keyword Coverage | 10% |

🔹 A realism rule ensures that resumes matching at least **50% of core skills never score below 60%**, mimicking industry ATS behavior.

---

## 📌 Example Output

- **ATS Score:** 72%
- **Why points were deducted:**
  - Missing core skill: Spring Boot
  - Low keyword overlap with job description
- **How to improve:**
  - Add a Spring Boot project
  - Rewrite experience using job description keywords

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **NLP:** TF-IDF, Cosine Similarity (scikit-learn)
- **PDF Parsing:** pdfplumber
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render
- **Version Control:** Git & GitHub

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
