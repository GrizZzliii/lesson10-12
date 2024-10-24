class CleaningHistory:
    def __init__(self, history_id: int, robot_id: int, date: str, rooms: list, status: str):
        self.history_id = history_id
        self.robot_id = robot_id
        self.date = date
        self.rooms = rooms  # список объектов Room
        self.status = status

    def __repr__(self):
        return f"CleaningHistory(id={self.history_id}, robot_id={self.robot_id}, date={self.date})"