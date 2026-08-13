# 🤖 AI Resume Matcher
# AI Resume Matcher

🔗 **Live Demo:** https://your-render-url.onrender.com

An ATS-style resume analysis web application that compares a resume with a job description and identifies matched and missing skills.

A Flask-based web application that analyzes a resume against a job description and calculates an ATS-style keyword match score.

The application supports both **PDF resume uploads** and **manual resume text input**.

---

## 🚀 Features

- 📄 Upload a resume in PDF format
- ✍️ Paste resume text manually
- 📋 Paste a job description
- 🎯 Calculate an ATS-style match score
- ✅ Display matched keywords
- ❌ Display missing keywords
- 💡 Generate resume improvement suggestions
- 🎨 Dynamic score colors based on the match percentage
- 📊 Visual progress bar for the match score
- 🔍 Extract text from PDF resumes using `pdfplumber`

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **pdfplumber**
- **Jinja2**

---

## 📂 Project Structure

```text
Resume Matcher/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
