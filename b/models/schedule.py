class Schedule:
    def __init__(self, schedule_id: int, date: str, time: str, rooms: list):
        self.schedule_id = schedule_id
        self.date = date
        self.time = time
        self.rooms = rooms  # список объектов Room

    def __repr__(self):
        return f"Schedule(id={self.schedule_id}, date={self.date}, time={self.time})"