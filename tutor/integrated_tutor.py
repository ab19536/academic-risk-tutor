from models.risk_model import predict_risk
from tutor.resource_mapper import get_resources
from tutor.virtual_tutor import generate_tutor_response


def run_integrated_tutor(
    student_name,
    ia1,
    ia2,
    assignment,
    attendance,
    course,
    weak_topic
):
    risk = predict_risk(
        ia1,
        ia2,
        assignment,
        attendance
    )

    resources = get_resources(risk["risk_level"])

    response = generate_tutor_response(
        student_name,
        course,
        risk["risk_level"],
        weak_topic,
        resources
    )

    return {
        "risk": risk,
        "resources": resources,
        "response": response
    }


if __name__ == "__main__":
    result = run_integrated_tutor(
        "Student 1",
        45,
        48,
        52,
        78,
        "Data Structures",
        "Arrays"
    )

    print("Integrated Academic Tutor")
    print("=" * 40)
    print("Risk:", result["risk"])
    print("Resources:", result["resources"])
    print()
    print(result["response"])
