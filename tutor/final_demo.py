from tutor.integrated_tutor import run_integrated_tutor
from tutor.response_checker import check_response


def run_demo():
    result = run_integrated_tutor(
        "Student Demo",
        45,
        48,
        52,
        78,
        "Data Structures",
        "Arrays"
    )

    quality = check_response(result["response"])

    print("=" * 60)
    print("ACADEMIC RISK PREDICTION + VIRTUAL TUTOR")
    print("=" * 60)

    print("\nStudent:", "Student Demo")
    print("Risk Result:", result["risk"])
    print("\nLearning Resources:")

    for resource in result["resources"]:
        print("-", resource)

    print("\nTutor Response:")
    print(result["response"])

    print("\nResponse Quality:")
    print("Acceptable:", quality["is_acceptable"])


if __name__ == "__main__":
    run_demo()
