KNOWLEDGE_BASE = {
    "Data Structures": {
        "Arrays": {
            "concepts": [
                "Array basics",
                "Array traversal",
                "Insertion and deletion",
                "Searching in arrays"
            ],
            "resources": [
                {
                    "title": "Array Basics and Operations",
                    "type": "Study Notes",
                    "difficulty": "Beginner"
                },
                {
                    "title": "Array Practice Problems",
                    "type": "Practice",
                    "difficulty": "Intermediate"
                }
            ]
        },
        "Linked Lists": {
            "concepts": [
                "Singly linked list",
                "Doubly linked list",
                "Insertion and deletion",
                "Linked list traversal"
            ],
            "resources": [
                {
                    "title": "Linked List Fundamentals",
                    "type": "Study Notes",
                    "difficulty": "Beginner"
                },
                {
                    "title": "Linked List Coding Exercises",
                    "type": "Practice",
                    "difficulty": "Intermediate"
                }
            ]
        },
        "Stacks and Queues": {
            "concepts": [
                "Stack operations",
                "Queue operations",
                "Applications of stacks",
                "Applications of queues"
            ],
            "resources": [
                {
                    "title": "Stacks and Queues Explained",
                    "type": "Study Notes",
                    "difficulty": "Beginner"
                },
                {
                    "title": "Stack and Queue Practice",
                    "type": "Practice",
                    "difficulty": "Intermediate"
                }
            ]
        },
        "Trees": {
            "concepts": [
                "Binary trees",
                "Tree traversal",
                "Binary search trees",
                "Tree operations"
            ],
            "resources": [
                {
                    "title": "Tree Data Structures",
                    "type": "Study Notes",
                    "difficulty": "Intermediate"
                },
                {
                    "title": "Tree Traversal Problems",
                    "type": "Practice",
                    "difficulty": "Advanced"
                }
            ]
        }
    }
}


def get_topic_resources(course, topic):
    course_data = KNOWLEDGE_BASE.get(course, {})
    topic_data = course_data.get(topic, {})
    return topic_data.get("resources", [])


if __name__ == "__main__":
    course = "Data Structures"
    topic = "Arrays"

    print("Course:", course)
    print("Topic:", topic)
    print("Learning Resources")
    print("-" * 30)

    for number, resource in enumerate(
        get_topic_resources(course, topic),
        start=1
    ):
        print(
            f"{number}. {resource['title']} "
            f"({resource['type']}, {resource['difficulty']})"
        )
