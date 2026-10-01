from tutor.virtual_tutor import generate_tutor_response


profiles = [
    {
        "student_name": "Student 1",
        "course": "Data Structures",
        "risk_level": "High",
        "weak_topic": "Arrays",
        "resources": [
            "Array Basics and Operations",
            "Array Practice Problems"
        ]
    },
    {
        "student_name": "Student 2",
        "course": "Data Structures",
        "risk_level": "Medium",
        "weak_topic": "Linked Lists",
        "resources": [
            "Linked List Fundamentals",
            "Linked List Coding Exercises"
        ]
    },
    {
        "student_name": "Student 3",
        "course": "Data Structures",
        "risk_level": "Low",
        "weak_topic": "Trees",
        "resources": [
            "Tree Data Structures",
            "Tree Traversal Problems"
        ]
    }
]


if __name__ == "__main__":
    for profile in profiles:
        print("=" * 60)

        response = generate_tutor_response(
            student_name=profile["student_name"],
            course=profile["course"],
            risk_level=profile["risk_level"],
            weak_topic=profile["weak_topic"],
            resources=profile["resources"]
        )

        print(response)
        print()
