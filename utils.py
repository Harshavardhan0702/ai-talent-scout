import random

# Extract skills from JD
def extract_skills(jd_text):
    skills_db = [
        "Python", "Machine Learning", "Flask", "Django", "SQL",
        "NLP", "React", "Java", "Spring Boot", "Data Analysis",
        "TensorFlow", "Docker", "Kubernetes", "Node.js"
    ]

    found_skills = [skill for skill in skills_db if skill.lower() in jd_text.lower()]
    return found_skills


# Match score + explainability
def calculate_match_score(candidate, required_skills):
    candidate_skills = set(candidate["skills"])
    required_skills = set(required_skills)

    matched = candidate_skills.intersection(required_skills)
    missing = required_skills - matched

    if len(required_skills) == 0:
        return 0, [], []

    score = (len(matched) / len(required_skills)) * 100

    return round(score, 2), list(matched), list(missing)


# Smarter interest simulation (NOT random anymore)
def simulate_interest(match_score):
    if match_score > 80:
        responses = [
            "This role aligns very well with my experience. I'm highly interested.",
            "Strong match with my skills. Happy to proceed further.",
            "This opportunity looks perfect for my background."
        ]
        score = random.randint(70, 90)

    elif match_score > 40:
        responses = [
            "This role looks interesting. Can you share more details?",
            "I might be a good fit. Open to discussion.",
            "Sounds good, but would like to know more."
        ]
        score = random.randint(40, 70)

    else:
        responses = [
            "Not a strong match for my profile currently.",
            "I don’t think this role aligns with my experience.",
            "Not interested at the moment."
        ]
        score = random.randint(10, 40)

    return random.choice(responses), score