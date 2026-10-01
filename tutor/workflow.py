def tutor_workflow():
    workflow = [
        "Collect student academic information",
        "Predict academic risk",
        "Identify weak learning areas",
        "Retrieve relevant learning resources",
        "Generate personalized study recommendations",
        "Provide step-by-step guidance",
        "Ask for student follow-up",
        "Update recommendations based on student progress"
    ]

    return workflow


if __name__ == "__main__":
    print("Virtual Tutor Workflow")
    print("-" * 30)

    for step_number, step in enumerate(tutor_workflow(), start=1):
        print(f"{step_number}. {step}")
