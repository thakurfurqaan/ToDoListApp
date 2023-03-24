from flask import request, jsonify
from src.models import Task, db

def register_routes(app):
    @app.route("/tasks", methods=["GET"])
    def get_all_tasks():
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])

    @app.route("/tasks", methods=["POST"])
    def add_task():
        task_name = request.json["name"]
        task = Task(name=task_name)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201

    @app.route("/tasks/<int:task_id>/complete", methods=["PUT"])
    def mark_task_complete(task_id):
        task = db.session.get(Task, task_id)  # Use Session.get() instead of Query.get()
        if task is None:
            return jsonify({"error": "Task not found"}), 404

        task.completed = True
        db.session.commit()
        return jsonify(task.to_dict())
