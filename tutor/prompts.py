def create_tutor_prompt(
    student_name,
    course,
    risk_level,
    weak_topic,
    resources
):
    resource_text = "\n".join(
        f"- {resource}" for resource in resources
    )

    prompt = f"""
You are a supportive academic virtual tutor.

Student: {student_name}
Course: {course}
Academic Risk Level: {risk_level}
Weak Topic: {weak_topic}

Available Learning Resources:
{resource_text}

Your task:
1. Explain why the student should focus on the weak topic.
2. Recommend a step-by-step study plan.
3. Start with the easiest concept.
4. Include practice activities.
5. Use the available learning resources.
6. Give a realistic short-term study goal.
7. End by asking the student what they would like to study first.

Keep the guidance personalized, clear, encouraging, and practical.
"""

    return prompt.strip()


if __name__ == "__main__":
    prompt = create_tutor_prompt(
        student_name="Student 1",
        course="Data Structures",
        risk_level="Medium",
        weak_topic="Arrays",
        resources=[
            "Array Basics and Operations",
            "Array Practice Problems"
        ]
    )

    print("Personalized Tutor Prompt")
    print("=" * 30)
    print(prompt)
