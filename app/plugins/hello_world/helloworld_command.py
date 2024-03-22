from app.commands.command.command import Command

class HelloWorldCommand(Command):
    def execute(self):
        return "Hello, World!"
    