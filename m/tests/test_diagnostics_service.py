import unittest
from business_logic.diagnostics_service import DiagnosticsService

class TestDiagnosticsService(unittest.TestCase):
    def setUp(self):
        self.diagnostics_service = DiagnosticsService()

    def test_run_full_diagnostics(self):
        result = self.diagnostics_service.run_full_diagnostics()
        self.assertIn("battery", result)
        self.assertIn("motor", result)
        self.assertEqual(result["status"], "healthy")

    def test_run_quick_diagnostics(self):
        result = self.diagnostics_service.run_quick_diagnostics()
        self.assertIn("battery", result)
        self.assertEqual(result["battery"], "good")