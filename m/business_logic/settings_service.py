class SettingsService:
    def __init__(self):
        self.settings = {"cleaning_mode": "auto"}

    def update_setting(self, key, value):
        self.settings[key] = value
        return self.settings