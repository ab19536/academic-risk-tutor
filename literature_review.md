
# Literature Review

## 1. Introduction

Educational data mining and learning analytics use student-related
data to understand learning processes and support educational
decision-making.

Machine learning techniques can identify patterns in assessment
records, while intelligent tutoring systems provide personalized
learning assistance.

Recent developments in large language models and retrieval-augmented
generation have introduced new ways to provide interactive,
course-specific educational support.

This project combines academic risk estimation with a syllabus-based
virtual tutor.

## 2. Educational Data Mining

Educational data mining focuses on applying data analysis and
machine learning techniques to educational datasets.

Romero and Ventura (2010) reviewed the development of educational
data mining and its applications, including student modelling,
prediction, and analysis of learning processes.

Relevance to this project:
- Academic assessment data can be analyzed to identify patterns.
- Classification algorithms can be explored for academic risk
  estimation.
- Data quality and appropriate evaluation are important.

## 3. Learning Analytics and Early Support

Siemens and Long (2011) discussed learning analytics and the use
of educational data to understand and improve learning.

Learning analytics can help institutions examine student progress
and identify opportunities for academic support.

Relevance to this project:
- Assessment results can inform supportive interventions.
- Dashboards can help present academic indicators.
- Predictions should support, not replace, human judgment.

## 4. Intelligent Tutoring Systems

VanLehn (2011) examined the effectiveness of human tutoring,
intelligent tutoring systems, and other instructional approaches.

Intelligent tutoring systems aim to provide individualized
instruction, feedback, and practice.

Relevance to this project:
- A virtual tutor can provide explanations and practice questions.
- Personalized guidance can be organized into manageable steps.
- Tutor responses need evaluation for correctness and usefulness.

## 5. Retrieval-Augmented Generation

Lewis et al. (2020) introduced retrieval-augmented generation,
which combines a language model with retrieved external knowledge.

In this project, syllabus documents and approved course notes
will serve as the retrieval knowledge source.

The system will retrieve relevant passages and provide them to
the LLM to help ground responses in course materials.

Relevance to this project:
- Course-specific context can be retrieved before generating
  an answer.
- Source passages can be shown to users.
- Retrieval does not guarantee factual correctness, so responses
  still require evaluation.

## 6. Summary

The reviewed work provides a foundation for educational data
analysis, academic support systems, intelligent tutoring, and
retrieval-augmented generation.

The proposed project combines these ideas in a prototype that
estimates academic risk and provides syllabus-grounded learning
recommendations.

The model and tutor will be evaluated separately because
predictive performance and educational answer quality are
different objectives.

## References

1. Romero, C., & Ventura, S. (2010).
   Educational data mining: A review of the state of the art.
   IEEE Transactions on Systems, Man, and Cybernetics,
   Part C: Applications and Reviews, 40(6), 601–618.

2. Siemens, G., & Long, P. (2011).
   Penetrating the fog: Analytics in learning and education.
   EDUCAUSE Review, 46(5), 30–40.

3. VanLehn, K. (2011).
   The relative effectiveness of human tutoring, intelligent
   tutoring systems, and other tutoring systems.
   Educational Psychologist, 46(4), 197–221.

4. Lewis, P., et al. (2020).
   Retrieval-augmented generation for knowledge-intensive NLP tasks.
   Advances in Neural Information Processing Systems, 33.