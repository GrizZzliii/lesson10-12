class ScheduleCleaningUseCase:
    def __init__(self, schedule_date: str, schedule_time: str):
        self.schedule_date = schedule_date
        self.schedule_time = schedule_time

    def execute(self, actor):
        print(f"{actor.name} настроил расписание на {self.schedule_date} в {self.schedule_time}")
        return f"Расписание настроено: {self.schedule_date} в {self.schedule_time}"