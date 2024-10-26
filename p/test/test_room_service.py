import unittest
from business_logic.room_service import RoomService

class TestRoomService(unittest.TestCase):

    def setUp(self):
        self.service = RoomService()

    def test_add_room(self):
        result = self.service.add_room(name="Living Room")
        self.assertTrue(result)

    def test_remove_room(self):
        self.service.add_room(name="Living Room")
        result = self.service.remove_room(room_id=1)
        self.assertTrue(result)

    def test_get_all_rooms(self):
        self.service.add_room(name="Living Room")
        rooms = self.service.get_all_rooms()
        self.assertGreater(len(rooms), 0)

if __name__ == '__main__':
    unittest.main()
