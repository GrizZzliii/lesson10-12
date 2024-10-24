class ViewStatisticsUseCase:
    def __init__(self, robot_id: int):
        self.robot_id = robot_id

    def execute(self, actor):
        # Логика для получения статистики уборки
        print(f"{actor.name} просматривает статистику робота {self.robot_id}")
        return f"Статистика для робота {self.robot_id} просмотрена"