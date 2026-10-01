def check_response(response):
    generic_phrases = [
        "study hard",
        "do your best",
        "keep studying",
        "work harder"
    ]

    inappropriate_phrases = [
        "you will definitely fail",
        "you are a bad student",
        "there is no hope"
    ]

    response_lower = response.lower()

    generic_found = [
        phrase for phrase in generic_phrases
        if phrase in response_lower
    ]

    inappropriate_found = [
        phrase for phrase in inappropriate_phrases
        if phrase in response_lower
    ]

    return {
        "generic_phrases": generic_found,
        "inappropriate_phrases": inappropriate_found,
        "is_acceptable": len(inappropriate_found) == 0
    }


if __name__ == "__main__":
    sample = "Review arrays and practice five questions."

    result = check_response(sample)

    print("Response Quality Check")
    print("=" * 30)
    print("Generic phrases:", result["generic_phrases"])
    print("Inappropriate phrases:", result["inappropriate_phrases"])
    print("Acceptable:", result["is_acceptable"])
