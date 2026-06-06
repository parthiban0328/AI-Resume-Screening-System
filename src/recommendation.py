def analyze_skills(resume_skills, job_skills):

    matched_skills = list(
        set(resume_skills).intersection(
            set(job_skills)
        )
    )

    missing_skills = list(
        set(job_skills) - set(resume_skills)
    )

    recommendations = []

    for skill in missing_skills:

        recommendations.append(
            f"Add projects or certifications related to {skill}"
        )

    return (
        matched_skills,
        missing_skills,
        recommendations
    )