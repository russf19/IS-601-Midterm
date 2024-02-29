#Master command class thats sets the structure of all commands

class Command:
    def execute(self):
        raise NotImplementedError("Commands MUST implement an execute method.")
    