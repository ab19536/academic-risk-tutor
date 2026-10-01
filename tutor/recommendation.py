from models.risk_model import predict_risk
from tutor.resource_mapper import get_resources


def get_student_recommendation(ia1, ia2, assignment, attendance):
    risk_result = predict_risk(
        ia1,
        ia2,
        assignment,
        attendance
    )

    resources = get_resources(risk_result["risk_level"])

    return {
        "academic_score": risk_result["academic_score"],
        "risk_level": risk_result["risk_level"],
        "resources": resources
    }


if __name__ == "__main__":
    result = get_student_recommendation(
        ia1=45,
        ia2=48,
        assignment=52,
        attendance=78
    )

    print("Academic Score:", result["academic_score"])
    print("Risk Level:", result["risk_level"])
    print("Recommended Resources:")

    for number, resource in enumerate(result["resources"], start=1):
        print(f"{number}. {resource}")
