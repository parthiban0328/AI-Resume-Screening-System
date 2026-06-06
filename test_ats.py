from src.ats_score import calculate_ats_score

resume = """
Java
Spring Boot
MySQL
"""

job = """
Need Java developer with Spring Boot and AWS
"""

score = calculate_ats_score(
    resume,
    job
)

print(score)