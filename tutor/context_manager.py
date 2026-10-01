def build_student_context(
    student_name,
    course,
    risk_level,
    weak_topics,
    completed_resources=None
):
    if completed_resources is None:
        completed_resources = []

    return {
        "student_name": student_name,
        "course": course,
        "risk_level": risk_level,
        "weak_topics": weak_topics,
        "completed_resources": completed_resources
    }


def get_context_summary(context):
    return (
        f"Student: {context['student_name']}\n"
        f"Course: {context['course']}\n"
        f"Risk Level: {context['risk_level']}\n"
        f"Weak Topics: {', '.join(context['weak_topics'])}\n"
        f"Completed Resources: "
        f"{', '.join(context['completed_resources']) or 'None'}"
    )


if __name__ == "__main__":
    context = build_student_context(
        "Student 1",
        "Data Structures",
        "Medium",
        ["Arrays", "Linked Lists"],
        ["Array Basics and Operations"]
    )

    print("Student Context")
    print("=" * 30)
    print(get_context_summary(context))
