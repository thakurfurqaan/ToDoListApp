import unittest
from flask_testing import TestCase
from app import app, db, Task

class ToDoListTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_tasks.db'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all_tasks(self):
        response = self.client.get("/tasks")
        self.assert200(response)
    def test_add_task(self):
        response = self.client.post("/tasks", json={"name": "Test Task"})
        self.assertStatus(response, 201)
        task_data = response.json
        self.assertEqual(task_data["name"], "Test Task")
        self.assertFalse(task_data["completed"])

    def test_mark_task_complete(self):
        task = Task(name="Test Task")
        db.session.add(task)
        db.session.commit()

        response = self.client.put(f"/tasks/{task.id}/complete")
        self.assert200(response)
        task_data = response.json
        self.assertEqual(task_data["id"], task.id)
        self.assertTrue(task_data["completed"])

    def test_get_all_tasks_data(self):
        task1 = Task(name="Test Task 1")
        task2 = Task(name="Test Task 2", completed=True)
        db.session.add(task1)
        db.session.add(task2)
        db.session.commit()

        response = self.client.get("/tasks")
        self.assert200(response)
        tasks_data = response.json
        self.assertEqual(len(tasks_data), 2)
        self.assertEqual(tasks_data[0]["name"], "Test Task 1")
        self.assertFalse(tasks_data[0]["completed"])
        self.assertEqual(tasks_data[1]["name"], "Test Task 2")
        self.assertTrue(tasks_data[1]["completed"])

    def test_mark_non_existent_task_complete(self):
        response = self.client.put("/tasks/999/complete")
        self.assert404(response)

if __name__ == "__main__":
    unittest.main()
