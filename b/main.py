from models import Robot, Room, Schedule, Service, CleaningHistory

# Создание робота
robot = Robot(robot_id=1, name="RoboCleaner", status="Ready", battery_level=100, filter_status="Clean", last_service_date="2024-09-01")

# Комнаты
kitchen = Room(room_id=1, name="Кухня")
living_room = Room(room_id=2, name="Гостиная")

# Расписание уборки
schedule = Schedule(schedule_id=1, date="2024-10-25", time="10:00", rooms=[kitchen, living_room])

# Сервисное обслуживание
service = Service(service_id=1, robot_id=robot.robot_id, last_service_date="2024-09-01", battery_level=100, filter_status="Clean")

# История уборок
history = CleaningHistory(history_id=1, robot_id=robot.robot_id, date="2024-10-20", rooms=[kitchen, living_room], status="Completed")

print(robot)
print(schedule)
print(service)
print(history)