
import unittest
from auth_service import register_user, users


class TestRegistration(unittest.TestCase):

    def setUp(self):
        users.clear()

    def test_successful_registration(self):
        result = register_user("alice@example.com", "password12345")
        self.assertEqual(result, "Registration successful")

    def test_duplicate_registration(self):
        register_user("alice@example.com", "password12345")
        result = register_user("alice@example.com", "password12345")
        self.assertEqual(result, "User already exists")

    def test_short_password(self):
        result = register_user("bob@example.com", "12345")
        self.assertEqual(result, "Password must be at least 12 characters")


if __name__ == "__main__":
    unittest.main()
