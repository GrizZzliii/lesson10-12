class Robot:
    def __init__(self, robot_id: int, name: str, status: str, battery_level: int, filter_status: str, last_service_date: str):
        self.robot_id = robot_id
        self.name = name
        self.status = status
        self.battery_level = battery_level
        self.filter_status = filter_status
        self.last_service_date = last_service_date

    def __repr__(self):
        return f"Robot(id={self.robot_id}, name={self.name}, status={self.status})"