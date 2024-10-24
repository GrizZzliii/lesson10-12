class Room:
    def __init__(self, room_id: int, name: str, is_cleaned: bool = False):
        self.room_id = room_id
        self.name = name
        self.is_cleaned = is_cleaned

    def __repr__(self):
        return f"Room(id={self.room_id}, name={self.name}, is_cleaned={self.is_cleaned})"