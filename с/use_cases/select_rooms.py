class SelectRoomsUseCase:
    def __init__(self, rooms: list):
        self.rooms = rooms

    def execute(self, actor):
        selected_rooms = ", ".join([room.name for room in self.rooms])
        print(f"{actor.name} выбрал комнаты: {selected_rooms} для уборки")
        return f"Выбраны комнаты: {selected_rooms}"