# 📄 Resume ATS Keyword Checker

A Python and Streamlit-based web application that analyzes a resume against a job description and provides an ATS match score, keyword analysis, resume section analysis, similarity score, improvement tips, and a downloadable PDF report.

## 🎯 Project Objective

The main objective of this project is to help job seekers understand how well their resume matches a particular job description.

The application identifies relevant keywords, missing skills, resume sections, and overall similarity between the resume and job description.

## ✨ Features

* 📄 Upload Resume in PDF or DOCX format
* 💼 Enter a Job Description
* 📊 Calculate ATS Match Score
* ✅ Identify Matching Keywords
* ❌ Identify Missing Keywords
* 💻 Analyze Technical Skills
* 🤝 Analyze Soft Skills
* 📋 Analyze Resume Sections
* 🤝 Calculate Resume–Job Description Similarity
* 📈 Resume Score Dashboard
* 🔍 Keyword Frequency Analysis
* 🎯 Resume Improvement Tips
* 📥 Download ATS Analysis Report as PDF
* 🎨 User-friendly Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* PyPDF2
* python-docx
* ReportLab
* Scikit-learn
* Regular Expressions
* TF-IDF
* Cosine Similarity

## ⚙️ How It Works

### 1. Upload Resume

The user uploads a resume in PDF or DOCX format.

### 2. Enter Job Description

The user pastes the required job description into the application.

### 3. Extract Resume Text

The application extracts text from the uploaded resume.

### 4. Keyword Analysis

The application checks for relevant technical and soft-skill keywords.

### 5. ATS Match Score

The application compares keywords found in the resume with keywords found in the job description.

### 6. Similarity Analysis

TF-IDF and cosine similarity are used to compare the overall text of the resume and job description.

### 7. Resume Section Analysis

The application checks for important sections such as:

* Contact Information
* Career Objective / Summary
* Education
* Skills
* Projects
* Certifications
* Experience
* Achievements

### 8. Improvement Suggestions

The application identifies missing keywords and provides suggestions that may help improve the resume.

### 9. PDF Report

The user can download an ATS analysis report containing the main results.

## 📊 Main Scores

The application provides:

* ATS Match Score
* Resume–Job Similarity Score
* Resume Section Coverage
* Overall Resume Score
* Matching Keyword Count
* Missing Keyword Count
* Technical Skill Count
* Soft Skill Count

## 📂 Project Structure

```text
Resume_ATS_Checker/
│
├── app.py
└── README.md
```

## ▶️ How to Run the Project

### 1. Install Required Libraries

Open PowerShell or Command Prompt and run:

```bash
pip install streamlit PyPDF2 python-docx reportlab scikit-learn
```

### 2. Open the Project Folder

```bash
cd "C:\Users\Jahnavi Palle\Desktop\Resume_ATS_Checker"
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open the Application

The application normally runs at:

```text
http://localhost:8501
```

## 🔍 Example Analysis

The application can produce results such as:

```text
ATS Match Score: 50%

Resume–Job Similarity: 17%

Section Coverage: 75%

Overall Resume Score: 47%
```

It also displays matching keywords, missing keywords, technical skills, soft skills, keyword frequency, and improvement suggestions.

## ⚠️ Important Note

The ATS score provided by this project is an analytical estimate based on the keywords and text patterns detected by the application.

It does not represent the exact scoring system used by a particular company's ATS.

Users should only add skills and keywords that genuinely match their knowledge, experience, and qualifications.

## 🔮 Future Enhancements

Possible future improvements include:

* AI-powered resume analysis
* Better skill extraction
* Resume formatting analysis
* Multiple job-description comparison
* Resume recommendations
* LinkedIn profile analysis
* Cloud deployment
* User accounts and analysis history
* More advanced NLP techniques

## 👩‍💻 Author

**Jahnavi P**

### Project

**Resume ATS Keyword Checker**

### Built With

**Python + Streamlit**
