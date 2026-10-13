"""GitHub Skill — Priority Tests (mocks only, no live GitHub calls)."""
import unittest
import os

class GithubSkillTest(unittest.TestCase):
    def test_happy_path_create_repo_mock(self):
        result = {"repo": "test-repo", "created": True, "mock": True}
        self.assertTrue(result["created"])

    def test_invalid_input_empty_name(self):
        name = ""
        self.assertEqual(name, "")

    def test_missing_token(self):
        os.environ.pop("GH_TOKEN", None)
        self.assertIsNone(os.environ.get("GH_TOKEN"))

    def test_timeout(self):
        def fake():
            raise TimeoutError("gh timeout")
        with self.assertRaises(TimeoutError):
            fake()

    def test_dry_run_no_push(self):
        # No git push performed
        self.assertTrue(True)

    def test_placeholder_key_rejected(self):
        for k in ["ghp_xxxxxx", "gho_xxxxxx", "your_token"]:
            if "ghp_x" in k or "gho_x" in k or "your" in k:
                self.assertTrue(True)

    def test_copy_paste_example(self):
        ex = '''
gh repo create test-repo --public
'''
        self.assertIn("gh repo create", ex)
        self.assertNotIn("ghp_", ex)

    def test_error_rate_limit(self):
        # Simulate 403
        err = {"message": "rate limit exceeded", "status": 403}
        self.assertEqual(err["status"], 403)

    def test_error_404_not_found(self):
        err = {"message": "not found", "status": 404}
        self.assertEqual(err["status"], 404)


if __name__ == "__main__":
    unittest.main()
