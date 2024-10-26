class ScheduleService:
    def __init__(self):
        self.schedule = []

    def add_cleaning_schedule(self, room, time):
        self.schedule.append({"room": room, "time": time})
        return True

    def get_schedule(self):
        return self.schedule