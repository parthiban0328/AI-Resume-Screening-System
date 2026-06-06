from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(
    resume_text,
    job_description,
    resume_skills,
    job_skills
):

    # Text Similarity Score
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [resume_text, job_description,]
    )

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    text_score = similarity * 100

    # Skill Match Score
    if len(job_skills) > 0:

        matched_count = len(
            set(resume_skills).intersection(
                set(job_skills)
            )
        )

        skill_score = (
            matched_count / len(job_skills)
        ) * 100

    else:
        skill_score = 0

    # Final ATS Score
    final_score = (
        skill_score * 0.7
        +
        text_score * 0.3
    )

    return round(final_score, 2)