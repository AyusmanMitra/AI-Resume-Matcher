# 🤖 AI Resume Matcher

An ATS-style resume analysis web application built with Python and Flask. It compares a candidate's resume against a job description and identifies matched and missing skills.

## 🔗 Live Demo

https://ai-resume-matcher-t7ig.onrender.com

- 📄 Upload resume as a PDF
- 📝 Paste resume text manually
- 💼 Paste job descriptions
- 📊 Calculate resume-to-job match score
- ✅ Identify matched keywords
- ❌ Identify missing keywords
- 💡 Generate suggestions to improve the resume
- 📱 Responsive web interface

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- pdfplumber
- Regular Expressions
- Git & GitHub
- Render

## ⚙️ How It Works

1. Upload your resume in PDF format.
2. Enter the job description.
3. The application extracts and cleans the resume text.
4. It compares keywords from the resume with keywords from the job description.
5. A match score is calculated.
6. The application displays:
   - Matching keywords
   - Missing keywords
   - Resume improvement suggestions

## 📁 Project Structure

```text
AI-Resume-Matcher/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css