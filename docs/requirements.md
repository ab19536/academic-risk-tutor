# System Requirements

## Functional Requirements
- FR1: Load or generate a structured assessment dataset.
- FR2: Validate feature values and handle missing data.
- FR3: Train and evaluate classification models.
- FR4: Accept student assessment indicators through a UI.
- FR5: Display a model-estimated probability and clearly state its limitations.
- FR6: Provide supportive study recommendations.
- FR7: Accept syllabus or course materials in PDF/TXT format.
- FR8: Retrieve relevant passages for a student's question.
- FR9: Generate a grounded tutor response when the LLM service is configured.
- FR10: Provide a fallback when the LLM API is unavailable.

## Non-Functional Requirements
- Usability: straightforward interface and clear language.
- Reproducibility: fixed seeds and documented setup.
- Privacy: data minimization and access control for any real records.
- Reliability: validate inputs and handle missing files/API errors.
- Transparency: explain that risk outputs are estimates.
- Maintainability: modular Python code and version control.

## Hardware
- Recommended: laptop/desktop with 8 GB RAM.
- Internet access for package installation and optional hosted LLM use.

## Software
- Python 3.10+
- VS Code or another Python IDE
- Git
- Pandas, NumPy, Scikit-learn, Streamlit
- Optional: OpenAI API access
