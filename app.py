import streamlit as st
import matplotlib.pyplot as plt

from src.pdf_parser import extract_text
from src.skill_extractor import extract_skills
from src.ats_score import calculate_ats_score
from src.recommendation import analyze_skills
from src.report_generator import generate_report

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# ----------------------------------
# HEADER
# ----------------------------------

st.title("📄 AI Resume Screening & ATS Analyzer")

st.markdown("""
Analyze your resume against a job description and get:

- ATS Match Score
- Matching Skills
- Missing Skills
- Improvement Suggestions
- Downloadable PDF Report
""")

st.divider()

# ----------------------------------
# INPUTS
# ----------------------------------

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=350
)

# ----------------------------------
# ANALYZE BUTTON
# ----------------------------------

if st.button("🚀 Analyze Resume"):

    if resume_file is None:
        st.warning("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please enter a job description.")
        st.stop()

    try:

        # Resume Text
        resume_text = extract_text(resume_file)

        # Skills
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        # ATS Score
        score = calculate_ats_score(
                resume_text,
                job_description,
                resume_skills,
                job_skills
        )

        # Analysis
        matched, missing, recommendations = analyze_skills(
            resume_skills,
            job_skills
        )

        st.divider()

        # ----------------------------------
        # ATS SCORE
        # ----------------------------------

        st.subheader("📊 ATS Score")

        st.metric(
            label="Match Score",
            value=f"{score}%"
        )

        st.progress(min(int(score), 100))
        if score >= 85:
             st.success("🌟 Excellent ATS Match")
        elif score >= 70:
             st.info("👍 Good ATS Match")
        elif score >= 50:
            st.warning("⚠️ Average ATS Match")
        else:
            st.error("❌ Low ATS Match")

        st.divider()

        # ----------------------------------
        # SMALL BAR CHART
        # ----------------------------------

        st.subheader("📈 Skill Analysis")

        fig, ax = plt.subplots(figsize=(4, 2))

        categories = [
            "Matched",
            "Missing"
        ]

        values = [
            len(matched),
            len(missing)
        ]

        ax.bar(
            categories,
            values
        )

        ax.set_ylabel("Skills")

        st.pyplot(
            fig,
            use_container_width=False
        )

        st.divider()

        # ----------------------------------
        # MATCHED / MISSING
        # ----------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Matched Skills")

            if matched:
                for skill in matched:
                    st.success(skill)

            else:
                st.write("No matching skills found.")

        with col2:

            st.subheader("❌ Missing Skills")

            if missing:
                for skill in missing:
                    st.error(skill)

            else:
                st.write("No missing skills.")

        st.divider()

        # ----------------------------------
        # RECOMMENDATIONS
        # ----------------------------------

        st.subheader("💡 Recommendations")

        if recommendations:

            for rec in recommendations:
                st.write("•", rec)

        else:

            st.success(
                "Excellent! Your resume matches all required skills."
            )

        st.divider()

        # ----------------------------------
        # PDF REPORT
        # ----------------------------------

        report_path = generate_report(
            score,
            matched,
            missing
        )

        with open(report_path, "rb") as file:

            st.download_button(
                label="📥 Download ATS Report",
                data=file,
                file_name="ATS_Report.pdf",
                mime="application/pdf"
            )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )