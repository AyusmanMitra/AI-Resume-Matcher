<<<<<<< HEAD
# 🤖 AI Resume Matcher
# AI Resume Matcher

🔗 **Live Demo:** https://your-render-url.onrender.com

An ATS-style resume analysis web application that compares a resume with a job description and identifies matched and missing skills.
=======
# AI Resume Matcher
>>>>>>> 145ec98 (Improve README documentation)

🔗 **Live Demo:** YOUR_RENDER_URL_HERE

An ATS-style resume analysis web application built with Python and Flask. It compares a candidate's resume against a job description and identifies matched and missing skills.

## 🚀 Features

- 📂 Upload resume as a PDF
- 📄 Paste resume text manually
- 📋 Paste job descriptions
- 🎯 Calculate ATS-style match score
- ✅ Identify matched skills
- ❌ Identify missing skills
- 💡 Generate resume improvement suggestions
- 🌐 Deployed as a live web application

## 🛠️ Technologies Used

- Python
- Flask
- pdfplumber
- HTML
- CSS
- Jinja2
- Git & GitHub
- Render

## ⚙️ How It Works

1. User uploads a PDF resume or enters resume text manually.
2. The application extracts and processes the resume content.
3. The user enters a job description.
4. Resume and job-description text are cleaned and converted into comparable words.
5. Common words are identified as matched skills.
6. Missing job-description terms are identified.
7. An ATS-style match percentage is calculated.
8. Suggestions are generated for missing terms.

## 📊 Matching System

The current version uses keyword-based text matching. Resume and job-description words are normalized and compared using Python sets.

The match score is calculated based on the number of common words relative to the number of words in the job description.

## 📁 Project Structure

AI-Resume-Matcher/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## 💻 Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Resume-Matcher
