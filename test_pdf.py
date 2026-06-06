from src.pdf_parser import extract_text

resume_text = extract_text(
    "sample_resumes/resume1.pdf"
)

print(resume_text)