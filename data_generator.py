import csv
import random
from pathlib import Path

FIELD_NAMES = [
    "cgpa",
    "backlogs",
    "coding_score",
    "aptitude_score",
    "communication_score",
    "projects",
    "internships",
    "certifications",
    "github_contributions",
    "leetcode_solved",
    "hackathon",
    "soft_skills",
    "placement_status",
    "placement_month",
]


def generate_student():
    cgpa = round(random.uniform(4.5, 10.0), 2)
    backlogs = random.choices(range(0, 6), weights=[50, 20, 12, 8, 6, 4])[0]
    coding_score = min(100, int(random.gauss(65, 18)))
    aptitude_score = min(100, int(random.gauss(60, 20)))
    communication_score = min(100, int(random.gauss(62, 18)))
    projects = random.choices(range(0, 16), weights=[10, 10, 15, 15, 12, 10, 8, 7, 6, 3, 2, 1, 1, 0, 0, 0])[0]
    internships = random.choices(range(0, 4), weights=[55, 30, 10, 5])[0]
    certifications = random.choices(range(0, 11), weights=[15, 15, 15, 12, 10, 9, 8, 7, 5, 3, 1])[0]
    github_contributions = abs(int(random.gauss(120, 150)))
    leetcode_solved = abs(int(random.gauss(70, 80)))
    hackathon = random.choices(range(0, 6), weights=[60, 20, 10, 5, 3, 2])[0]
    soft_skills = min(100, int(random.gauss(65, 18)))
    score_components = (
        cgpa * 8
        + coding_score * 0.3
        + aptitude_score * 0.25
        + communication_score * 0.2
        + projects * 4
        + internships * 5
        + certifications * 1.5
        + min(150, github_contributions) * 0.15
        + min(120, leetcode_solved) * 0.1
        + hackathon * 4
        + soft_skills * 0.15
        - backlogs * 6
    )
    probability = max(0, min(1, (score_components / 250)))
    placement_status = 1 if random.random() < probability else 0
    placement_month = random.randint(1, 12) if placement_status else random.randint(6, 12)
    return {
        "cgpa": cgpa,
        "backlogs": backlogs,
        "coding_score": coding_score,
        "aptitude_score": aptitude_score,
        "communication_score": communication_score,
        "projects": projects,
        "internships": internships,
        "certifications": certifications,
        "github_contributions": github_contributions,
        "leetcode_solved": leetcode_solved,
        "hackathon": hackathon,
        "soft_skills": soft_skills,
        "placement_status": placement_status,
        "placement_month": placement_month,
    }


def main():
    path = Path("data.csv")
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writeheader()
        for _ in range(5000):
            writer.writerow(generate_student())
    print(f"Generated {path.absolute()}")


if __name__ == "__main__":
    main()
