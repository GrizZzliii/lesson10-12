import unittest
from business_logic.schedule_service import ScheduleService

class TestScheduleService(unittest.TestCase):
    def setUp(self):
        self.schedule_service = ScheduleService()

    def test_add_schedule_entry(self):
        result = self.schedule_service.add_schedule("Kitchen", "8:00 AM")
        self.assertTrue(result)
        self.assertEqual(len(self.schedule_service.get_schedule()), 1)

    def test_remove_schedule_entry(self):
        self.schedule_service.add_schedule("Kitchen", "8:00 AM")
        result = self.schedule_service.remove_schedule("Kitchen", "8:00 AM")
        self.assertTrue(result)
        self.assertEqual(len(self.schedule_service.get_schedule()), 0)

    def test_get_empty_schedule(self):
        self.assertEqual(self.schedule_service.get_schedule(), [])