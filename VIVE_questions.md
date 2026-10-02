# 🎤 Resume ATS Keyword Checker — Viva Questions & Answers

## 1. What is your project?

My project is a Resume ATS Keyword Checker. It compares a resume with a job description and identifies matching keywords, missing keywords, skills, resume sections, and similarity.

## 2. What is ATS?

ATS stands for Applicant Tracking System. It is software used by organizations to help screen and manage resumes during recruitment.

## 3. Why did you choose this project?

I chose this project because many job applicants want to know whether their resume matches a particular job description. My project provides a simple way to analyze this.

## 4. What programming language did you use?

I used Python because it has many useful libraries for text processing, machine learning, PDF processing, and web application development.

## 5. Why did you use Streamlit?

I used Streamlit because it allows us to create a web application using Python without requiring a separate front-end framework.

## 6. What file formats does your project support?

The project supports PDF and DOCX resume files.

## 7. How does your project calculate the ATS Match Score?

The project detects keywords from the job description and checks how many of those keywords are also present in the resume.

The basic formula is:

ATS Score = Matching Keywords / Total Job Keywords × 100

## 8. What are matching keywords?

Matching keywords are keywords that are found both in the job description and in the resume.

## 9. What are missing keywords?

Missing keywords are relevant keywords detected in the job description but not found in the resume.

## 10. What is TF-IDF?

TF-IDF stands for Term Frequency–Inverse Document Frequency.

It is a technique used to represent the importance of words in documents.

## 11. What is cosine similarity?

Cosine similarity measures how similar two text documents are based on their TF-IDF representations.

In my project, it is used to compare the resume with the job description.

## 12. How do you extract text from a PDF?

I use the PyPDF2 library to read the PDF and extract text from its pages.

## 13. How do you read a DOCX file?

I use the python-docx library to read text from paragraphs in a DOCX document.

## 14. What is keyword frequency analysis?

Keyword frequency analysis counts how many times detected job-description keywords appear in the resume.

## 15. What is Resume Section Analysis?

It checks whether important sections such as Education, Skills, Projects, Certifications, Experience, and Achievements are present in the resume.

## 16. What is the Overall Resume Score?

The Overall Resume Score is calculated using the ATS Match Score, Resume–Job Similarity Score, and Section Coverage.

## 17. How do you generate the PDF report?

I use the ReportLab library to create a downloadable PDF containing the analysis results.

## 18. What are the main technologies used?

The main technologies are:

* Python
* Streamlit
* PyPDF2
* python-docx
* Scikit-learn
* ReportLab
* Regular Expressions

## 19. What are the advantages of your project?

The project is simple to use, supports PDF and DOCX files, analyzes keywords and sections, calculates similarity, provides improvement tips, and generates a PDF report.

## 20. What are the limitations of your project?

The ATS score is an analytical estimate and may not exactly match the scoring system of a particular company's ATS.

The project mainly uses predefined keywords and text-based analysis.

## 21. What are the future enhancements?

Future enhancements could include:

* AI-powered resume analysis
* Better skill extraction
* Resume formatting analysis
* Cloud deployment
* More advanced NLP techniques
* Multiple job-description comparison

## 22. What did you learn from this project?

I learned how to build a Python web application using Streamlit, process PDF and DOCX files, perform keyword analysis, use TF-IDF and cosine similarity, generate PDF reports, and organize a complete software project.

## ⭐ Short Project Explanation

If the interviewer says:

**"Explain your project in 1 minute."**

You can say:

> My project is a Resume ATS Keyword Checker developed using Python and Streamlit. It allows users to upload a PDF or DOCX resume and paste a job description. The application extracts the resume text, identifies matching and missing keywords, calculates an ATS match score, analyzes technical and soft skills, checks important resume sections, and calculates resume–job similarity using TF-IDF and cosine similarity. It also provides improvement suggestions and allows the user to download the analysis as a PDF report.
