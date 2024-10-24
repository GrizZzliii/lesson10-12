class Actor:
    def __init__(self, actor_id: int, name: str, role: str):
        self.actor_id = actor_id
        self.name = name
        self.role = role

    def __repr__(self):
        return f"Actor(id={self.actor_id}, name={self.name}, role={self.role})"

    def perform_action(self, use_case):
        return use_case.execute(self)