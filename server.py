from flask import Flask, request, jsonify
from educhain_tools import generate_mcqs, generate_lesson_plan

app = Flask(__name__)

@app.route('/tool/mcqs', methods=['POST'])
def mcq_tool():
    data = request.json
    topic = data.get("topic", "Python Basics")
    num = data.get("num_questions", 5)
    result = generate_mcqs(topic, num)
    return jsonify(result)

@app.route('/resource/lessonplan', methods=['POST'])
def lesson_plan_resource():
    data = request.json
    subject = data.get("subject", "Algebra")
    result = generate_lesson_plan(subject)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
