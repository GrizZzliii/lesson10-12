class CleaningProgramUseCase:
    def __init__(self, program_name: str):
        self.program_name = program_name

    def execute(self, actor):
        print(f"{actor.name} запускает программу уборки: {self.program_name}")
        return f"Запущена программа уборки: {self.program_name}"