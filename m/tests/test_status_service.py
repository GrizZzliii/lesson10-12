import unittest
from business_logic.status_service import StatusService

class TestStatusService(unittest.TestCase):
    def setUp(self):
        self.status_service = StatusService()

    def test_update_status(self):
        self.status_service.update_status("active")
        self.assertEqual(self.status_service.get_status(), "active")

    def test_initial_status(self):
        self.assertEqual(self.status_service.get_status(), "idle")