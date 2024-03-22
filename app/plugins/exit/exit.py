import sys
from app.commands.command.command import Command

class ExitCommand(Command):
    def execute(self):
        print("Shutting down...")
        sys.exit(0)
