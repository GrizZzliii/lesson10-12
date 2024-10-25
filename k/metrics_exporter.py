from prometheus_client import start_http_server, Gauge
from collector import Collector

class MetricsExporter:
    def __init__(self, collector):
        self.collector = collector
        self.gauges = {
            "availability": Gauge("component_availability", "Availability of components", ["component"]),
            "response_time": Gauge("component_response_time", "Response time of components", ["component"])
        }

    def export_metrics(self):
        """Экспортирует метрики в Prometheus."""
        metrics = self.collector.get_metrics()
        for component, data in metrics.items():
            self.gauges["availability"].labels(component=component).set(data["is_available"])
            self.gauges["response_time"].labels(component=component).set(data["response_time"])

    def start_exporting(self, port=8000):
        """Запускает сервер для экспорта метрик."""
        start_http_server(port)
        print(f"Metrics are being exported at http://localhost:{port}")
        while True:
            self.export_metrics()
