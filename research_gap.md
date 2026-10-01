
# Research Gap and Proposed Contribution

## 1. Existing Approaches

Educational data mining research explores the use of academic
records for understanding student performance.

Learning analytics systems provide dashboards and indicators
to support academic monitoring.

Intelligent tutoring systems provide explanations, practice,
and individualized feedback.

Retrieval-augmented generation connects LLM responses to
retrieved external documents, such as course materials.

## 2. Project Motivation

For this project, we aim to bring academic risk estimation
and syllabus-grounded tutoring into one educational prototype.

The system will explore how assessment indicators can be
used to suggest supportive learning actions and how retrieved
course content can help a virtual tutor provide relevant
study recommendations.

## 3. Preliminary Research Gap

The project will investigate the integration of the following
functions within one prototype:

1. Academic risk estimation from internal assessment data.
2. Identification of potential learning gaps from assessment
   indicators and student input.
3. Retrieval of syllabus-specific content for tutoring.
4. Generation of step-by-step study recommendations.
5. Presentation of model estimates and tutor guidance in
   a unified dashboard.

This is a preliminary integration gap for the proposed
implementation, not a claim that no existing system provides
these functions.

A broader literature search and comparison of existing
systems will be required to establish research novelty.

## 4. Proposed Contribution

The planned contribution is a reproducible educational
prototype integrating:

- Supervised machine learning for academic risk estimation.
- Syllabus document retrieval for course-specific context.
- An LLM tutor for explanations and study recommendations.
- A web dashboard for student-facing academic support.
- Separate evaluation of model performance and tutor quality.

## 5. Evaluation Plan

The ML component will be evaluated using a held-out test set
and metrics such as precision, recall, F1-score, PR-AUC,
ROC-AUC, and calibration.

The tutor component will be evaluated for relevance,
syllabus grounding, citation correctness, and usefulness.

The initial synthetic dataset will be used for software
development and demonstration only. Real-world validity
requires appropriate institutional data and external
evaluation.