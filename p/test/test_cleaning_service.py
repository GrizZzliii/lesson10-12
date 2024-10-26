import unittest
from business_logic.cleaning_service import CleaningService

class TestCleaningService(unittest.TestCase):

    def setUp(self):
        self.service = CleaningService()

    def test_start_cleaning(self):
        result = self.service.start_cleaning(room_id=1)
        self.assertTrue(result)
        
    def test_stop_cleaning(self):
        self.service.start_cleaning(room_id=1)
        result = self.service.stop_cleaning(room_id=1)
        self.assertTrue(result)

    def test_get_cleaning_status(self):
        self.service.start_cleaning(room_id=1)
        status = self.service.get_cleaning_status(room_id=1)
        self.assertEqual(status, "Cleaning")

if __name__ == '__main__':
    unittest.main()
