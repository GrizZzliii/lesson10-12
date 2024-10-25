from collector import Collector
from health_check import HealthCheck
from metrics_exporter import MetricsExporter
import time

if __name__ == "__main__":
    collector = Collector()
    health_check = HealthCheck(collector)
    metrics_exporter = MetricsExporter(collector)

    # Запускаем экспорт метрик в фоновом режиме
    metrics_exporter.start_exporting(port=8000)

    # Запускаем проверки компонентов каждые 10 секунд
    while True:
        health_check.run_checks()
        time.sleep(10)
