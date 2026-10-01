from tutor.integrated_tutor import run_integrated_tutor


scenarios = [
    {
        "name": "High Risk Student",
        "student": "Student 1",
        "ia1": 35,
        "ia2": 40,
        "assignment": 42,
        "attendance": 65,
        "topic": "Arrays"
    },
    {
        "name": "Medium Risk Student",
        "student": "Student 2",
        "ia1": 55,
        "ia2": 60,
        "assignment": 58,
        "attendance": 75,
        "topic": "Linked Lists"
    },
    {
        "name": "Low Risk Student",
        "student": "Student 3",
        "ia1": 80,
        "ia2": 82,
        "assignment": 85,
        "attendance": 90,
        "topic": "Trees"
    }
]


if __name__ == "__main__":
    for scenario in scenarios:
        result = run_integrated_tutor(
            scenario["student"],
            scenario["ia1"],
            scenario["ia2"],
            scenario["assignment"],
            scenario["attendance"],
            "Data Structures",
            scenario["topic"]
        )

        print("=" * 60)
        print(scenario["name"])
        print("Risk Result:", result["risk"])
        print("Resources:", result["resources"])
