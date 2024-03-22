from app.commands.command.command import Command
from app.plugins.calculation.calculation import CalculationCommand
from app.plugins.history.history import History

class AddCommand(Command):
    def execute(self, a, b):
        return CalculationCommand.add(a, b)

class SubtractCommand(Command):
    def execute(self, a, b):
        return CalculationCommand.subtract(a, b)

class MultiplyCommand(Command):
    def execute(self, a, b):
        return CalculationCommand.multiply(a, b)

class DivideCommand(Command):
    def execute(self, a, b):
        return CalculationCommand.divide(a, b)
    
class GetHistoryCommand(Command):
    def execute(self):
        history = History.get_history()
        return "\n".join(history) if history else "No history to view."

class AddHistoryCommand(Command):
    def execute(self, record):
        History.add_history(record)
        return "Added to history."

class DeleteHistoryCommand(Command):
    def execute(self):
        History.clear_history()
        return "History erased."
    