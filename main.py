from flask import Flask, jsonify, request

app = Flask(__name__)

todos = ["test"]

@app.route("/", methods=["GET"])
def get_status():
    return jsonify({"status": "ok"})

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data.get("task")
    if task:
        todos.append(task)
        return jsonify({"message": "Task added", "task": task}), 201
    return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
