import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load student data
data = pd.read_csv("data/student_data.csv")

print("Student Dataset:")
print(data.head())

# Input features
features = [
    "internal_1",
    "internal_2",
    "attendance",
    "assignment_score",
    "study_hours"
]

X = data[features]
y = data["risk"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create the model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# Test with a new student
new_student = pd.DataFrame({
    "internal_1": [45],
    "internal_2": [48],
    "attendance": [72],
    "assignment_score": [55],
    "study_hours": [1]
})

# Predict risk
prediction = model.predict(new_student)

print("\nNew Student Academic Risk:", prediction[0])