import unittest
from business_logic.user_service import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.service = UserService()

    def test_register_user(self):
        result = self.service.register_user(username="test_user", password="test_password")
        self.assertTrue(result)

    def test_login_user(self):
        self.service.register_user(username="test_user", password="test_password")
        result = self.service.login(username="test_user", password="test_password")
        self.assertTrue(result)

    def test_logout_user(self):
        self.service.register_user(username="test_user", password="test_password")
        self.service.login(username="test_user", password="test_password")
        result = self.service.logout(username="test_user")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
