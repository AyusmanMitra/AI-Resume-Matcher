from flask import Flask, render_template, request
import pdfplumber
import re

app = Flask(__name__)
def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def calculate_match(resume, job_desc):
    skill_aliases = {
        "python": ["python"],
        "java": ["java"],
        "c": ["c", "c programming", "c language"],
        "c++": ["c++", "cpp", "c plus plus"],
        "javascript": ["javascript", "js"],
        "html": ["html", "html5"],
        "css": ["css", "css3"],
        "sql": ["sql"],
        "flask": ["flask"],
        "django": ["django"],
        "react": ["react", "react.js", "reactjs"],
        "node.js": ["node", "node.js", "nodejs"],
        "aws": ["aws", "amazon web services"],
        "docker": ["docker"],
        "git": ["git", "github"],
        "mongodb": ["mongodb", "mongo db"],
        "mysql": ["mysql"],
        "bootstrap": ["bootstrap"],
        "streamlit": ["streamlit"],
        "flutter": ["flutter"],
        "php": ["php"],
        "typescript": ["typescript", "ts"],
        "angular": ["angular"],
        "vue": ["vue", "vue.js"],
        "spring": ["spring"],
        "spring boot": ["spring boot"],
        "kotlin": ["kotlin"],
        "swift": ["swift"],
        "tensorflow": ["tensorflow"],
        "pytorch": ["pytorch"],
        "pandas": ["pandas"],
        "numpy": ["numpy"],
        "linux": ["linux"],
        "rest api": ["rest api", "restful api"],
        "machine learning": ["machine learning", "ml"],
        "deep learning": ["deep learning", "dl"],
        "data science": ["data science"],
        "communication": ["communication"],
        "teamwork": ["teamwork"]
    }

    skill_categories = {
        "Programming": [
            "python", "java", "c", "c++", "javascript",
            "typescript", "php", "kotlin", "swift"
        ],

        "Web Development": [
            "html", "css"
        ],

        "Frameworks & Libraries": [
            "flask", "django", "react", "node.js",
            "angular", "vue", "spring", "spring boot",
            "bootstrap", "streamlit", "flutter"
        ],

        "Databases": [
            "sql", "mysql", "mongodb"
        ],

        "Cloud & DevOps": [
            "aws", "docker", "git"
        ],

        "AI & Data Science": [
            "machine learning", "deep learning", "data science",
            "tensorflow", "pytorch", "pandas", "numpy"
        ],

        "Operating Systems": [
            "linux"
        ],

        "APIs": [
            "rest api"
        ],

        "Soft Skills": [
            "communication", "teamwork"
        ]
    }

    resume_lower = resume.lower()
    job_lower = job_desc.lower()

    matched = set()
    missing = set()

    def contains_skill(text, skill):

        pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"

        return re.search(pattern, text, re.IGNORECASE) is not None

    for category, skills in skill_categories.items():

        for skill in skills:

            job_has_skill = contains_skill(job_lower, skill)

            if job_has_skill:

                resume_has_skill = contains_skill(resume_lower, skill)

                if resume_has_skill:
                    matched.add(skill)
                else:
                    missing.add(skill)

    total_required = len(matched) + len(missing)

    if total_required > 0:
        match_score = (len(matched) / total_required) * 100
    else:
        match_score = 0

    category_scores = {}

    for category, skills in skill_categories.items():

        category_required = [
            skill for skill in skills
            if skill in matched or skill in missing
        ]

        if category_required:
            category_matched = [
                skill for skill in category_required
                if skill in matched
            ]

            category_score = (
                len(category_matched) / len(category_required)
            ) * 100

            category_scores[category] = round(category_score, 2)

    return round(match_score, 2), matched, missing, category_scores


@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    matched = None
    missing = None
    category_scores = {}
    suggestions = []
    error = None

    if request.method == "POST":

        resume_file = request.files.get("resume_file")
        resume_text = request.form.get("resume", "").strip()
        job_desc = request.form.get("job_desc", "").strip()

        # Check job description
        if not job_desc:
            error = "Please enter a job description."

        # Check resume
        elif resume_file and resume_file.filename != "":

            if not resume_file.filename.lower().endswith(".pdf"):
                error = "Please upload a PDF resume."

            else:
                try:
                    resume = extract_text_from_pdf(resume_file)

                    if not resume.strip():
                        error = "Could not extract text from this PDF. Try an ATS-friendly PDF or paste your resume text."

                except Exception as e:
                    error = "There was a problem reading the PDF."

        elif resume_text:
            resume = resume_text

        else:
            error = "Please upload a PDF resume or paste your resume text."

        # Run matching only if there is no error
        if error is None:

            score, matched, missing, category_results = calculate_match(
                resume,
                job_desc
            )

            for skill in sorted(missing):
                suggestions.append(
                    f"Consider adding {skill.title()} to your resume if you have relevant experience."
                )

    # Score color
    if score is not None:

        if score >= 70:
            score_color = "#28a745"

        elif score >= 40:
            score_color = "#ff9800"

        else:
            score_color = "#dc3545"

    else:
        score_color = "#28a745"

    return render_template(
        "index.html",
        score=score,
        matched=matched,
        missing=missing,
        category_results=category_results,
        suggestions=suggestions,
        score_color=score_color,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)