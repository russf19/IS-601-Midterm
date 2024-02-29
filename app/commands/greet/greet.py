from app.commands.command.command import Command

class GreetCommand(Command):
    def execute(self):
        return "Hello, world!"
    