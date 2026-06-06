import json

with open(
    "assets/skills_database.json",
    "r"
) as file:

    skills_db = json.load(file)["skills"]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:

        if skill in text:

            found_skills.append(skill)

    return list(set(found_skills))