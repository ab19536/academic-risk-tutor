from tutor.prompts import create_tutor_prompt


def generate_tutor_response(
    student_name,
    course,
    risk_level,
    weak_topic,
    resources
):
    prompt = create_tutor_prompt(
        student_name,
        course,
        risk_level,
        weak_topic,
        resources
    )

    response = f"""
Personalized Virtual Tutor Response
===================================

Hello {student_name}!

Your current academic risk level is: {risk_level}

You should focus on: {weak_topic}

Study Plan:
1. Review the basic concepts of {weak_topic}.
2. Use the beginner learning resource first.
3. Practice simple questions.
4. Review your mistakes.
5. Move to intermediate practice.

Recommended Resources:
"""

    for number, resource in enumerate(resources, start=1):
        response += f"{number}. {resource}\n"

    response += f"""
Short-term Goal:
Complete the basic concepts of {weak_topic} and solve 5 practice questions.

Next Step:
What would you like to study first?

Tutor Prompt:
{prompt}
"""

    return response.strip()


if __name__ == "__main__":
    result = generate_tutor_response(
        student_name="Student 1",
        course="Data Structures",
        risk_level="Medium",
        weak_topic="Arrays",
        resources=[
            "Array Basics and Operations",
            "Array Practice Problems"
        ]
    )

    print(result)
