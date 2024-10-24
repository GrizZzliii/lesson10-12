from use_cases import Actor, ConnectRobotUseCase, SelectRoomsUseCase, CleaningProgramUseCase, ScheduleCleaningUseCase, ViewStatisticsUseCase
from models import Room

# Актор (Пользователь)
user = Actor(actor_id=1, name="Иван", role="Пользователь")

# Сценарий: Подключение робота к Wi-Fi
connect_use_case = ConnectRobotUseCase(robot_id=1, wifi_ssid="Home_WiFi", wifi_password="password123")
print(user.perform_action(connect_use_case))

# Сценарий: Выбор комнат для уборки
kitchen = Room(room_id=1, name="Кухня")
living_room = Room(room_id=2, name="Гостиная")
select_rooms_use_case = SelectRoomsUseCase(rooms=[kitchen, living_room])
print(user.perform_action(select_rooms_use_case))

# Сценарий: Запуск программы уборки
cleaning_program_use_case = CleaningProgramUseCase(program_name="Полная уборка")
print(user.perform_action(cleaning_program_use_case))

# Сценарий: Настройка расписания
schedule_use_case = ScheduleCleaningUseCase(schedule_date="2024-10-25", schedule_time="10:00")
print(user.perform_action(schedule_use_case))

# Сценарий: Просмотр статистики уборок
view_stats_use_case = ViewStatisticsUseCase(robot_id=1)
print(user.perform_action(view_stats_use_case))