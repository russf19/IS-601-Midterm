from app.commands.command.command import Command
#deleted test class
class GreetCommand(Command):
    def execute(self):
        return "Welcome to my calculator! To get started type a command and numbers. If you want to exit, type 'exit'."
    