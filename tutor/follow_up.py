def generate_follow_up(
    student_name,
    weak_topic,
    completed=False
):
    if completed:
        return (
            f"Great work, {student_name}! "
            f"You completed the {weak_topic} activity. "
            f"Next, try five intermediate practice questions."
        )

    return (
        f"{student_name}, continue working on {weak_topic}. "
        f"Start with one basic concept, then solve three practice questions. "
        f"Tell me which question you found difficult."
    )


if __name__ == "__main__":
    print(generate_follow_up(
        "Student 1",
        "Arrays",
        completed=False
    ))
