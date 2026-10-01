from tutor.virtual_tutor import generate_tutor_response


def evaluate_response(response, risk_level, weak_topic):
    checks = {
        "risk_level_present": risk_level in response,
        "weak_topic_present": weak_topic in response,
        "study_plan_present": "Study Plan:" in response,
        "resources_present": "Recommended Resources:" in response,
        "goal_present": "Short-term Goal:" in response,
        "follow_up_present": "Next Step:" in response
    }

    score = sum(checks.values())

    return {
        "score": score,
        "total": len(checks),
        "checks": checks
    }


if __name__ == "__main__":
    response = generate_tutor_response(
        student_name="Student 1",
        course="Data Structures",
        risk_level="Medium",
        weak_topic="Arrays",
        resources=[
            "Array Basics and Operations",
            "Array Practice Problems"
        ]
    )

    result = evaluate_response(response, "Medium", "Arrays")

    print("Response Evaluation")
    print("=" * 30)
    print(f"Score: {result['score']}/{result['total']}")

    for check, value in result["checks"].items():
        print(f"{check}: {'PASS' if value else 'FAIL'}")
