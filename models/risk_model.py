def predict_risk(ia1, ia2, assignment, attendance):
    """
    Predict academic risk using internal assessment,
    assignment and attendance information.
    """

    academic_score = (
        ia1 * 0.30
        + ia2 * 0.30
        + assignment * 0.20
        + attendance * 0.20
    )

    if academic_score < 50:
        risk_level = "High"
    elif academic_score < 70:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "academic_score": round(academic_score, 2),
        "risk_level": risk_level
    }


if __name__ == "__main__":
    result = predict_risk(
        ia1=45,
        ia2=48,
        assignment=52,
        attendance=78
    )

    print("Academic Score:", result["academic_score"])
    print("Risk Level:", result["risk_level"])
