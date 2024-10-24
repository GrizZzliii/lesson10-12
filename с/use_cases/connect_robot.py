class ConnectRobotUseCase:
    def __init__(self, robot_id: int, wifi_ssid: str, wifi_password: str):
        self.robot_id = robot_id
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password

    def execute(self, actor):
        # Логика подключения робота к Wi-Fi сети
        print(f"{actor.name} подключает робота {self.robot_id} к сети {self.wifi_ssid}")
        return f"Робот {self.robot_id} подключен к {self.wifi_ssid}"