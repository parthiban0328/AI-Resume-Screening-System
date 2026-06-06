from src.skill_extractor import extract_skills

text = """
Java
Spring Boot
MySQL
GitHub
"""

skills = extract_skills(text)

print(skills)