from app.commands.command.command import Command

class GoodbyeCommand(Command):
    def execute(self):
        return "Goodbye."
    