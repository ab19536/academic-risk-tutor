## Project Details

Student Name: YOUR NAME
Department: YOUR DEPARTMENT
College: YOUR COLLEGE
Academic Year: 2026-2027
Project Duration: 15 Days
# Day 1 — Project Planning and Problem Definition

## 1. Project Title

**AI-Based Student Academic Risk Prediction and Personalized Learning Recommendation System Using Machine Learning and LLMs**

## 2. Background

Educational institutions collect internal assessment marks, quiz scores, assignment results, and attendance records. These indicators may help identify students who could benefit from timely academic support. Reviewing this information manually can be time-consuming, and students may not always receive individualized guidance aligned with their course syllabus.

Machine learning can be explored to estimate academic risk from historical assessment patterns. A large language model (LLM), combined with retrieval from official course materials, can support students with explanations and structured study plans.

## 3. Problem Statement

Students experiencing academic difficulties may not receive timely, individualized support before final examinations. Existing manual review processes can make it difficult to consistently identify assessment-related learning gaps and connect students with syllabus-specific study resources.

The proposed project will develop a prototype that uses machine learning to estimate academic risk from internal assessment data and an LLM-based virtual tutor to provide step-by-step, syllabus-grounded study recommendations. The system is intended to support learning and educator review, not to make consequential decisions about students.

## 4. Aim

To design and implement a Python-based academic support prototype that combines machine-learning risk estimation with a syllabus-grounded virtual tutor.

## 5. Objectives

1. Create or prepare a structured dataset containing internal assessment marks and relevant academic indicators.
2. Perform data validation, preprocessing, and exploratory data analysis.
3. Train Logistic Regression and Random Forest classification models.
4. Evaluate models using precision, recall, F1-score, ROC-AUC, PR-AUC, and confusion matrices, where appropriate.
5. Build a web interface for entering assessment information and viewing model estimates.
6. Identify potential learning gaps from student-provided or assessment-related information.
7. Ingest syllabus documents and retrieve relevant passages for tutor responses.
8. Generate step-by-step study recommendations and practice prompts.
9. Document privacy, fairness, limitations, and the need for human oversight.

## 6. Scope

### Included

- Synthetic data for initial development and testing.
- Internal assessment, quiz, assignment, attendance, and other justified academic features.
- Binary classification for a clearly defined academic outcome.
- Comparison of baseline machine-learning models.
- Streamlit dashboard.
- Syllabus PDF/TXT ingestion and retrieval.
- Optional LLM API integration with a fallback when the API is unavailable.
- Model and tutor evaluation documentation.

### Excluded from the initial prototype

- Automated grading or student discipline.
- Admissions, scholarship, or other high-impact decisions.
- Claims that the model determines a student's ability or future with certainty.
- Direct integration with institutional ERP/LMS systems.
- Use of identifiable student records without authorization and safeguards.

## 7. Intended Users

| User | Intended use |
|---|---|
| Student | Review an estimate, explore learning gaps, ask syllabus-related questions, and use a study plan |
| Faculty/advisor | Review indicators and provide supportive academic guidance |
| Project administrator | Manage approved course materials and appropriately protected data |

## 8. Expected Outcomes

- A reproducible Python project.
- A synthetic academic dataset and documented data schema.
- Trained and evaluated baseline ML models.
- A risk-estimation interface with supportive recommendations.
- A syllabus retrieval and LLM tutoring module.
- A Streamlit demonstration dashboard.
- Project report, testing evidence, and presentation materials.

## 9. Success Criteria

The project will be considered technically complete when:

- Data generation and preprocessing run reproducibly.
- Models train and produce documented holdout metrics.
- The app accepts valid input and returns a model estimate.
- Uploaded course materials can be searched for relevant passages.
- Tutor responses use retrieved passages when available and disclose when course evidence is missing.
- Core workflows and failure cases are tested.
- Documentation explains limitations and responsible use.

No target model score is promised in advance. Results must be reported from actual experiments, and synthetic-data performance must not be presented as evidence of real-world validity.

## 10. Day 1 Deliverables

- Project title and problem statement.
- Aim, objectives, and scope.
- Intended users and expected outcomes.
- Initial technology stack and system workflow.
- Requirements and architecture documents.
- GitHub repository initialized with project documentation.
