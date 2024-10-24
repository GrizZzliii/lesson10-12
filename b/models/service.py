class Service:
    def __init__(self, service_id: int, robot_id: int, last_service_date: str, battery_level: int, filter_status: str):
        self.service_id = service_id
        self.robot_id = robot_id
        self.last_service_date = last_service_date
        self.battery_level = battery_level
        self.filter_status = filter_status

    def __repr__(self):
        return f"Service(id={self.service_id}, robot_id={self.robot_id})"