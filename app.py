
import streamlit as st
import re
from reportlab.pdfgen import canvas
from io import BytesIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Resume ATS Keyword Checker",
    page_icon="📄",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    h1 {
        font-size: 42px !important;
        font-weight: 700 !important;
    }

    h2 {
        font-size: 30px !important;
        margin-top: 25px !important;
    }

    h3 {
        font-size: 22px !important;
    }

    /* Metric box */
    div[data-testid="stMetric"] {
        background-color: #f5f7fa;
        border: 1px solid #e1e5ea;
        padding: 15px;
        border-radius: 12px;
    }

    /* FIX: Make metric numbers visible */
    [data-testid="stMetricValue"] {
        color: black !important;
        font-size: 28px !important;
        font-weight: 700 !important;
    }

    /* FIX: Make metric labels visible */
    [data-testid="stMetricLabel"] {
        color: black !important;
        font-weight: 600 !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        margin-top: 40px;
        color: #777;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TITLE
# =========================================================

st.title("📄 Resume ATS Keyword Checker")

st.write(
    "🚀 Analyze your resume against a job description "
    "and discover keywords, skills, sections, similarity, "
    "and improvement areas."
)


# =========================================================
# RESUME UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf", "docx"]
)


# =========================================================
# JOB DESCRIPTION
# =========================================================

job_description = st.text_area(
    "💼 Paste the Job Description",
    height=200,
    placeholder="Paste the job description here..."
)


# =========================================================
# PDF TEXT EXTRACTION
# =========================================================

def extract_pdf_text(file):

    try:

        from PyPDF2 import PdfReader

        reader = PdfReader(file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception:

        return ""


# =========================================================
# DOCX TEXT EXTRACTION
# =========================================================

def extract_docx_text(file):

    try:

        from docx import Document

        document = Document(file)

        text = ""

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

        return text

    except Exception:

        return ""


# =========================================================
# RESUME TEXT EXTRACTION
# =========================================================

def extract_resume_text(file):

    if file.name.lower().endswith(".pdf"):

        return extract_pdf_text(file)

    elif file.name.lower().endswith(".docx"):

        return extract_docx_text(file)

    return ""


# =========================================================
# NORMALIZE TEXT
# =========================================================

def normalize_text(text):

    text = text.lower()

    text = text.replace(
        "data structures and algorithms",
        "data structures algorithms"
    )

    text = text.replace(
        "problem-solving",
        "problem solving"
    )

    return text


# =========================================================
# KEYWORD DETECTION
# =========================================================

def find_keywords(text):

    text = normalize_text(text)

    keywords = [

        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "html",
        "css",
        "sql",
        "mysql",
        "database",
        "git",
        "github",
        "data structures",
        "algorithms",
        "dsa",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "ai",
        "django",
        "flask",
        "react",
        "node.js",
        "node",
        "excel",
        "power bi",
        "cloud",
        "aws",
        "azure",
        "communication",
        "teamwork",
        "problem solving"

    ]

    found_keywords = []

    for keyword in keywords:

        if keyword == "c":

            if re.search(
                r"\bc\b",
                text
            ):

                found_keywords.append(keyword)

        elif keyword == "c++":

            # FIXED C++ regex
            if re.search(
                r"c\+\+",
                text
            ):

                found_keywords.append(keyword)

        elif keyword == "node.js":

            if "node.js" in text:

                found_keywords.append(keyword)

        elif keyword == "ai":

            if re.search(
                r"\bai\b",
                text
            ):

                found_keywords.append(keyword)

        else:

            if keyword in text:

                found_keywords.append(keyword)

    return found_keywords


# =========================================================
# RESUME-JOB DESCRIPTION SIMILARITY
# =========================================================

def calculate_similarity(
    resume_text,
    job_description
):

    try:

        documents = [
            resume_text,
            job_description
        ]

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        tfidf_matrix = vectorizer.fit_transform(
            documents
        )

        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        similarity_score = round(
            similarity * 100
        )

        return similarity_score

    except Exception:

        return 0


# =========================================================
# PDF REPORT
# =========================================================

def create_pdf_report(
    score,
    matching_keywords,
    missing_keywords,
    technical_skills,
    soft_skills,
    section_score,
    similarity_score,
    overall_score
):

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)

    y = 800

    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawString(
        50,
        y,
        "Resume ATS Analysis Report"
    )

    y -= 40

    pdf.setFont(
        "Helvetica",
        12
    )

    pdf.drawString(
        50,
        y,
        f"ATS Match Score: {score}%"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"Resume-Job Similarity: {similarity_score}%"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"Section Coverage: {section_score}%"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"Overall Resume Score: {overall_score}%"
    )

    y -= 40


    # -----------------------------------------------------
    # MATCHING KEYWORDS
    # -----------------------------------------------------

    pdf.setFont(
        "Helvetica-Bold",
        13
    )

    pdf.drawString(
        50,
        y,
        "Matching Keywords:"
    )

    y -= 20

    pdf.setFont(
        "Helvetica",
        10
    )

    if matching_keywords:

        for keyword in matching_keywords:

            pdf.drawString(
                60,
                y,
                f"- {keyword}"
            )

            y -= 15

            if y < 50:

                pdf.showPage()

                y = 800

                pdf.setFont(
                    "Helvetica",
                    10
                )

    else:

        pdf.drawString(
            60,
            y,
            "None"
        )

        y -= 20


    # -----------------------------------------------------
    # MISSING KEYWORDS
    # -----------------------------------------------------

    y -= 15

    pdf.setFont(
        "Helvetica-Bold",
        13
    )

    pdf.drawString(
        50,
        y,
        "Missing Keywords:"
    )

    y -= 20

    pdf.setFont(
        "Helvetica",
        10
    )

    if missing_keywords:

        for keyword in missing_keywords:

            pdf.drawString(
                60,
                y,
                f"- {keyword}"
            )

            y -= 15

            if y < 50:

                pdf.showPage()

                y = 800

                pdf.setFont(
                    "Helvetica",
                    10
                )

    else:

        pdf.drawString(
            60,
            y,
            "None"
        )

        y -= 20


    # -----------------------------------------------------
    # TECHNICAL SKILLS
    # -----------------------------------------------------

    y -= 15

    pdf.setFont(
        "Helvetica-Bold",
        13
    )

    pdf.drawString(
        50,
        y,
        "Technical Skills:"
    )

    y -= 20

    pdf.setFont(
        "Helvetica",
        10
    )

    if technical_skills:

        for skill in technical_skills:

            pdf.drawString(
                60,
                y,
                f"- {skill}"
            )

            y -= 15

    else:

        pdf.drawString(
            60,
            y,
            "None"
        )

        y -= 20


    # -----------------------------------------------------
    # SOFT SKILLS
    # -----------------------------------------------------

    y -= 15

    pdf.setFont(
        "Helvetica-Bold",
        13
    )

    pdf.drawString(
        50,
        y,
        "Soft Skills:"
    )

    y -= 20

    pdf.setFont(
        "Helvetica",
        10
    )

    if soft_skills:

        for skill in soft_skills:

            pdf.drawString(
                60,
                y,
                f"- {skill}"
            )

            y -= 15

    else:

        pdf.drawString(
            60,
            y,
            "None"
        )


    pdf.save()

    buffer.seek(0)

    return buffer


# =========================================================
# MAIN ANALYSIS
# =========================================================

if uploaded_file and job_description:

    resume_text = extract_resume_text(
        uploaded_file
    )

    if resume_text:

        st.success(
            "✅ Resume uploaded and text extracted successfully!"
        )


        # =================================================
        # EXTRACTED TEXT
        # =================================================

        with st.expander(
            "📄 View Extracted Resume Text"
        ):

            st.write(
                resume_text
            )


        # =================================================
        # KEYWORDS
        # =================================================

        resume_keywords = find_keywords(
            resume_text
        )

        job_keywords = find_keywords(
            job_description
        )


        matching_keywords = [

            keyword

            for keyword in job_keywords

            if keyword in resume_keywords

        ]


        missing_keywords = [

            keyword

            for keyword in job_keywords

            if keyword not in resume_keywords

        ]


        # =================================================
        # ATS SCORE
        # =================================================

        if len(job_keywords) > 0:

            score = round(

                (
                    len(matching_keywords)
                    / len(job_keywords)
                ) * 100

            )

        else:

            score = 0


        # =================================================
        # SIMILARITY SCORE
        # =================================================

        similarity_score = calculate_similarity(

            resume_text,

            job_description

        )


        # =================================================
        # ATS ANALYSIS
        # =================================================

        st.divider()

        st.header(
            "📊 ATS Analysis"
        )


        st.metric(
            "ATS Match Score",
            f"{score}%"
        )


        # =================================================
        # KEYWORD METRICS
        # =================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "✅ Matched Keywords",
                len(matching_keywords)
            )


        with col2:

            st.metric(
                "❌ Missing Keywords",
                len(missing_keywords)
            )


        with col3:

            st.metric(
                "🔑 Total Job Keywords",
                len(job_keywords)
            )


        st.progress(
            score / 100
        )


        if score >= 80:

            st.success(
                "🎉 Strong ATS match!"
            )

        elif score >= 60:

            st.info(
                "👍 Good ATS match, but there is room for improvement."
            )

        else:

            st.warning(
                "⚠️ Your resume needs more relevant keywords."
            )


        # =================================================
        # SIMILARITY ANALYSIS
        # =================================================

        st.divider()

        st.header(
            "🤝 Resume–Job Description Similarity"
        )

        st.write(
            "This score compares the overall text of your "
            "resume with the job description using TF-IDF "
            "and cosine similarity."
        )


        similarity_col1, similarity_col2 = st.columns(2)


        with similarity_col1:

            st.metric(
                "🤝 Similarity Score",
                f"{similarity_score}%"
            )


        with similarity_col2:

            if similarity_score >= 70:

                st.success(
                    "🟢 High text similarity"
                )

            elif similarity_score >= 40:

                st.info(
                    "🟡 Moderate text similarity"
                )

            else:

                st.warning(
                    "🔴 Low text similarity"
                )


        st.progress(
            similarity_score / 100
        )


        # =================================================
        # TECHNICAL SKILLS
        # =================================================

        technical_skill_list = [

            "python",
            "java",
            "c",
            "c++",
            "javascript",
            "html",
            "css",
            "sql",
            "mysql",
            "database",
            "git",
            "github",
            "data structures",
            "algorithms",
            "dsa",
            "machine learning",
            "deep learning",
            "artificial intelligence",
            "django",
            "flask",
            "react",
            "node.js",
            "node",
            "excel",
            "power bi",
            "cloud",
            "aws",
            "azure"

        ]


        technical_skills = [

            keyword

            for keyword in matching_keywords

            if keyword in technical_skill_list

        ]


        # =================================================
        # SOFT SKILLS
        # =================================================

        soft_skill_list = [

            "communication",
            "teamwork",
            "problem solving"

        ]


        soft_skills = [

            keyword

            for keyword in matching_keywords

            if keyword in soft_skill_list

        ]


        # =================================================
        # RESUME STRENGTH
        # =================================================

        st.divider()

        st.header(
            "💪 Resume Strength Analysis"
        )


        keyword_coverage = score


        st.write(
            f"Your resume matches approximately "
            f"**{keyword_coverage}%** of the detected "
            f"job-description keywords."
        )


        if keyword_coverage >= 80:

            st.success(
                "🟢 Strong keyword coverage"
            )

        elif keyword_coverage >= 60:

            st.info(
                "🟡 Moderate keyword coverage"
            )

        else:

            st.warning(
                "🔴 Low keyword coverage"
            )


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "💻 Technical Skills"
            )


            if technical_skills:

                for skill in technical_skills:

                    st.write(
                        f"✅ {skill}"
                    )

            else:

                st.write(
                    "No matching technical skills found."
                )


        with col2:

            st.subheader(
                "🤝 Soft Skills"
            )


            if soft_skills:

                for skill in soft_skills:

                    st.write(
                        f"✅ {skill}"
                    )

            else:

                st.write(
                    "No matching soft skills found."
                )


        # =================================================
        # RESUME SECTION ANALYSIS
        # =================================================

        st.divider()

        st.header(
            "📋 Resume Section Analysis"
        )


        resume_text_lower = resume_text.lower()


        resume_sections = {

            "Contact Information": [

                "email",
                "phone",
                "mobile",
                "linkedin"

            ],

            "Career Objective / Summary": [

                "objective",
                "summary",
                "profile"

            ],

            "Education": [

                "education",
                "academic",
                "degree",
                "b.tech",
                "bachelor"

            ],

            "Skills": [

                "skills",
                "technical skills",
                "programming skills"

            ],

            "Projects": [

                "projects",
                "project"

            ],

            "Certifications": [

                "certification",
                "certifications",
                "certificate"

            ],

            "Experience": [

                "experience",
                "internship",
                "work experience"

            ],

            "Achievements": [

                "achievements",
                "achievement",
                "awards"

            ]

        }


        found_sections = []

        missing_sections = []


        for section, section_keywords in resume_sections.items():

            found = any(

                keyword in resume_text_lower

                for keyword in section_keywords

            )


            if found:

                found_sections.append(
                    section
                )

            else:

                missing_sections.append(
                    section
                )


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "✅ Sections Found"
            )


            for section in found_sections:

                st.write(
                    f"✅ {section}"
                )


            if not found_sections:

                st.write(
                    "No major sections detected."
                )


        with col2:

            st.subheader(
                "❌ Sections Missing"
            )


            for section in missing_sections:

                st.write(
                    f"❌ {section}"
                )


            if not missing_sections:

                st.success(
                    "🎉 All important sections detected!"
                )


        # =================================================
        # SECTION SCORE
        # =================================================

        total_sections = len(
            resume_sections
        )


        section_score = round(

            (
                len(found_sections)
                / total_sections
            ) * 100

        )


        st.subheader(
            "📊 Resume Section Coverage"
        )


        st.progress(
            section_score / 100
        )


        st.write(
            f"Your resume contains "
            f"**{len(found_sections)} out of "
            f"{total_sections}** important sections "
            f"({section_score}%)."
        )


        # =================================================
        # RESUME SCORE DASHBOARD
        # =================================================

        st.divider()

        st.header(
            "📈 Resume Score Dashboard"
        )


        technical_skill_count = len(
            technical_skills
        )


        soft_skill_count = len(
            soft_skills
        )


        col1, col2, col3, col4, col5 = st.columns(5)


        with col1:

            st.metric(
                "📊 ATS Score",
                f"{score}%"
            )


        with col2:

            st.metric(
                "🤝 Similarity",
                f"{similarity_score}%"
            )


        with col3:

            st.metric(
                "📋 Sections",
                f"{section_score}%"
            )


        with col4:

            st.metric(
                "💻 Technical Skills",
                technical_skill_count
            )


        with col5:

            st.metric(
                "🤝 Soft Skills",
                soft_skill_count
            )


        # =================================================
        # OVERALL SCORE
        # =================================================

        overall_score = round(

            (
                score
                + similarity_score
                + section_score
            ) / 3

        )


        st.subheader(
            "🏆 Overall Resume Score"
        )


        st.progress(
            overall_score / 100
        )


        st.write(
            f"Your overall resume score is "
            f"**{overall_score}%**."
        )


        # =================================================
        # SCORE CHART
        # =================================================

        st.subheader(
            "📊 Resume Score Comparison"
        )


        chart_data = {

            "ATS Score": score,

            "Similarity": similarity_score,

            "Section Coverage": section_score,

            "Overall Score": overall_score

        }


        st.bar_chart(
            chart_data
        )


        # =================================================
        # KEYWORD FREQUENCY
        # =================================================

        st.divider()

        st.header(
            "🔍 Keyword Frequency Analysis"
        )


        st.write(
            "This shows how many times detected job "
            "keywords appear in your resume."
        )


        resume_text_normalized = normalize_text(
            resume_text
        )


        keyword_frequency = {}


        for keyword in job_keywords:

            if keyword == "c":

                count = len(

                    re.findall(
                        r"\bc\b",
                        resume_text_normalized
                    )

                )

            elif keyword == "c++":

                # FIXED C++ frequency regex
                count = len(

                    re.findall(
                        r"c\+\+",
                        resume_text_normalized
                    )

                )

            elif keyword == "ai":

                count = len(

                    re.findall(
                        r"\bai\b",
                        resume_text_normalized
                    )

                )

            else:

                count = resume_text_normalized.count(
                    keyword
                )


            keyword_frequency[keyword] = count


        if keyword_frequency:

            for keyword, count in keyword_frequency.items():

                col1, col2 = st.columns([3, 1])


                with col1:

                    st.write(
                        f"🔹 **{keyword}**"
                    )


                with col2:

                    st.write(
                        f"**{count}** mention(s)"
                    )

        else:

            st.info(
                "No job-description keywords were detected."
            )


        # =================================================
        # MATCHING KEYWORDS
        # =================================================

        st.divider()

        st.header(
            "✅ Matching Keywords"
        )


        if matching_keywords:

            for keyword in matching_keywords:

                st.write(
                    f"✅ {keyword}"
                )

        else:

            st.warning(
                "No matching keywords found."
            )


        # =================================================
        # MISSING KEYWORDS
        # =================================================

        st.header(
            "❌ Missing Keywords"
        )


        if missing_keywords:

            for keyword in missing_keywords:

                st.write(
                    f"❌ {keyword}"
                )

        else:

            st.success(
                "🎉 No missing keywords!"
            )


        # =================================================
        # SKILLS TO LEARN
        # =================================================

        st.divider()

        st.header(
            "📚 Skills You May Need to Learn"
        )


        if missing_keywords:

            st.write(
                "Only learn or add skills that genuinely "
                "match your experience and goals."
            )


            for keyword in missing_keywords:

                st.write(
                    f"📌 {keyword}"
                )

        else:

            st.success(
                "🎉 No major missing keywords detected!"
            )


        # =================================================
        # IMPROVEMENT TIPS
        # =================================================

        st.divider()

        st.header(
            "🎯 Resume Improvement Tips"
        )


        tips = []


        if "python" in missing_keywords:

            tips.append(
                "Consider learning Python if it is required "
                "for your target roles."
            )


        if (
            "sql" in missing_keywords
            or "mysql" in missing_keywords
        ):

            tips.append(
                "Consider learning SQL and basic database concepts."
            )


        if (
            "git" in missing_keywords
            or "github" in missing_keywords
        ):

            tips.append(
                "Learn Git and GitHub for version control."
            )


        if (
            "data structures" in missing_keywords
            or "dsa" in missing_keywords
        ):

            tips.append(
                "Practice Data Structures and Algorithms."
            )


        if "algorithms" in missing_keywords:

            tips.append(
                "Study common algorithms and "
                "problem-solving techniques."
            )


        if "communication" in missing_keywords:

            tips.append(
                "Highlight genuine communication experience "
                "from projects, presentations, or teamwork."
            )


        if similarity_score < 40:

            tips.append(
                "Try tailoring your resume wording to "
                "genuinely relevant terminology from the job description."
            )


        if not tips:

            tips.append(
                "Keep your resume focused on skills, "
                "projects, and experience that you genuinely have."
            )


        for tip in tips:

            st.write(
                f"👉 {tip}"
            )


        # =================================================
        # PDF DOWNLOAD
        # =================================================

        st.divider()

        st.header(
            "📥 Download ATS Report"
        )


        pdf_report = create_pdf_report(

            score,

            matching_keywords,

            missing_keywords,

            technical_skills,

            soft_skills,

            section_score,

            similarity_score,

            overall_score

        )


        st.download_button(

            label="📥 Download ATS Report PDF",

            data=pdf_report,

            file_name="ATS_Resume_Report.pdf",

            mime="application/pdf"

        )


    else:

        st.error(
            "Could not extract text from the resume. "
            "Please try another PDF or DOCX file."
        )


elif uploaded_file or job_description:

    st.warning(
        "Please provide both your resume and the job description."
    )


else:

    st.info(
        "👆 Upload your resume and paste a job description to begin."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        📄 Resume ATS Keyword Checker |
        Built with Python & Streamlit

    </div>
    """,
    unsafe_allow_html=True
)

