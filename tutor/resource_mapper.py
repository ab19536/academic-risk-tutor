def get_resources(risk_level):
    resources = {
        "High": [
            "Review basic concepts from the course syllabus",
            "Practice solved examples",
            "Attend additional faculty/tutorial sessions"
        ],
        "Medium": [
            "Review weak concepts from the course syllabus",
            "Practice topic-wise questions",
            "Complete additional learning exercises"
        ],
        "Low": [
            "Continue regular revision",
            "Practice advanced questions",
            "Review upcoming course topics"
        ]
    }

    return resources.get(risk_level, [])


if __name__ == "__main__":
    risk_level = "Medium"

    print("Risk Level:", risk_level)
    print("Recommended Learning Resources")
    print("-" * 35)

    for number, resource in enumerate(get_resources(risk_level), start=1):
        print(f"{number}. {resource}")
