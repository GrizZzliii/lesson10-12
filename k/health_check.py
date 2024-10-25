import time
from collector import Collector

class HealthCheck:
    def __init__(self, collector):
        self.collector = collector

    def check_component(self, component_name, check_function):
        """Проверяет компонент с помощью переданной функции."""
        start_time = time.time()
        is_available = check_function()
        response_time = time.time() - start_time

        # Записываем результаты проверки в Collector
        self.collector.collect_status(component_name, is_available, response_time)

    def run_checks(self):
        """Запуск проверок для всех компонентов."""
        self.check_component("API Gateway", self.mock_check_api_gateway)
        self.check_component("Business Logic", self.mock_check_business_logic)
        self.check_component("Data Layer", self.mock_check_data_layer)

    def mock_check_api_gateway(self):
        # Здесь будет реальная логика проверки
        return True

    def mock_check_business_logic(self):
        # Здесь будет реальная логика проверки
        return True

    def mock_check_data_layer(self):
        # Здесь будет реальная логика проверки
        return True
