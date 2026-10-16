import os
import tempfile
import unittest
from app import create_app

class LearnForgeApiTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp.name, "test.sqlite3")
        self.app = create_app({"TESTING": True, "DATABASE": self.db_path})
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp.cleanup()


    def test_course_module_returns_learning_content(self):
        response = self.client.get("/api/courses/1/modules/101")
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertTrue(payload["content"])
        self.assertGreaterEqual(len(payload["key_points"]), 1)
        self.assertTrue(payload["practice"])

    def test_completing_lesson_updates_course_progress(self):
        response = self.client.post("/api/courses/3/modules/301/complete", json={})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()["completed"])
        self.assertGreater(self.client.get("/api/courses/3").get_json()["progress"], 0)

    def test_notifications_have_a_welcome_state(self):
        response = self.client.get("/api/notifications")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.get_json()["items"]), 1)

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_course_search_filters_results(self):
        response = self.client.get("/api/courses?q=python")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertGreaterEqual(data["total"], 1)
        self.assertTrue(all("python" in c["title"].lower() or "python" in c["description"].lower() or "python" in " ".join(c["skills"]).lower() for c in data["items"]))

    def test_missing_course_returns_404(self):
        self.assertEqual(self.client.get("/api/courses/999").status_code, 404)

    def test_progress_rejects_out_of_range(self):
        response = self.client.post("/api/progress", json={"course_id": 1, "progress": 101})
        self.assertEqual(response.status_code, 400)

    def test_progress_persists_between_requests(self):
        response = self.client.post("/api/progress", json={"course_id": 1, "progress": 57})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get("/api/courses/1").get_json()["progress"], 57)

    def test_quiz_submission_scores_and_records_attempt(self):
        response = self.client.post("/api/quiz/submit", json={"answers": {"1": 1, "2": 2, "3": 1}})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["score"], 3)
        self.assertEqual(response.get_json()["percent"], 100)
        self.assertEqual(len(self.client.get("/api/quiz/attempts").get_json()["items"]), 1)

    def test_quiz_rejects_invalid_option_index(self):
        response = self.client.post("/api/quiz/submit", json={"answers": {"1": 999}})
        self.assertEqual(response.status_code, 400)


    def test_notes_create_update_delete(self):
        created = self.client.post("/api/notes", json={
            "title": "Loops", "body": "Review for quiz", "course_id": 1, "tags": ["python"]
        })
        self.assertEqual(created.status_code, 201)
        note_id = created.get_json()["item"]["id"]
        self.assertEqual(self.client.get("/api/notes").get_json()["total"], 1)
        updated = self.client.put(f"/api/notes/{note_id}", json={
            "title": "Loops review", "body": "Practice examples", "tags": ["revision"]
        })
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.get_json()["item"]["title"], "Loops review")
        self.assertEqual(self.client.delete(f"/api/notes/{note_id}").status_code, 200)
        self.assertEqual(self.client.get("/api/notes").get_json()["total"], 0)

    def test_notes_validate_required_fields(self):
        self.assertEqual(self.client.post("/api/notes", json={"title": "", "body": "text"}).status_code, 400)

    def test_bookmarks_can_be_saved_and_removed(self):
        saved = self.client.put("/api/bookmarks/1", json={"saved": True})
        self.assertEqual(saved.status_code, 200)
        self.assertEqual(self.client.get("/api/bookmarks").get_json()["total"], 1)
        self.client.put("/api/bookmarks/1", json={"saved": False})
        self.assertEqual(self.client.get("/api/bookmarks").get_json()["total"], 0)

    def test_study_session_can_be_completed(self):
        created = self.client.post("/api/study-sessions", json={
            "day": "Friday", "topic": "Revision", "duration_minutes": 30
        })
        session_id = created.get_json()["item"]["id"]
        changed = self.client.patch(f"/api/study-sessions/{session_id}", json={"completed": True})
        self.assertEqual(changed.status_code, 200)
        self.assertEqual(changed.get_json()["item"]["completed"], 1)

    def test_study_session_create_list_delete(self):
        created = self.client.post("/api/study-sessions", json={"day": "Thursday", "topic": "Python", "duration_minutes": 30})
        self.assertEqual(created.status_code, 201)
        item = created.get_json()["item"]
        self.assertEqual(item["topic"], "Python")
        self.assertEqual(len(self.client.get("/api/study-sessions").get_json()["items"]), 1)
        deleted = self.client.delete(f'/api/study-sessions/{item["id"]}')
        self.assertEqual(deleted.status_code, 200)
        self.assertEqual(len(self.client.get("/api/study-sessions").get_json()["items"]), 0)

if __name__ == "__main__":
    unittest.main()
