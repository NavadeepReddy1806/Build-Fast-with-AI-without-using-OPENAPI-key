#Note: The questions are just sample ones and i'll submit the version using OpenApi also
def generate_mcqs(topic: str, num_questions: int = 5):
    questions = []
    for i in range(1, num_questions + 1):
        questions.append({
            "question": f"What is question {i} on {topic}?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A"
        })
    return {"topic": topic, "mcqs": questions}

def generate_lesson_plan(subject: str):
    plan = {
        "title": f"Lesson Plan for {subject}",
        "objectives": [
            f"Understand basic concepts of {subject}",
            f"Apply {subject} to solve problems"
        ],
        "activities": [
            "Interactive discussion",
            "Hands-on exercises",
            "Group activity"
        ],
        "assessment": [
            "Quiz",
            "Mini project"
        ]
    }
    return {"subject": subject, "lesson_plan": plan}
