from app.commands.command.command import Command
from app.plugins.calculation.calculation import CalculationCommand
from app.plugins.history.history import History

class AddCommand(Command):
    def execute(self, a, b):
        result = CalculationCommand.add(a, b)
        History.add_history('Add', a, b, result)
        return result

class SubtractCommand(Command):
    def execute(self, a, b):
        result = CalculationCommand.subtract(a, b)
        History.add_history('Subtract', a, b, result)
        return result

class MultiplyCommand(Command):
    def execute(self, a, b):
        result = CalculationCommand.multiply(a, b)
        History.add_history('Multiply', a, b, result)
        return result

class DivideCommand(Command):
    def execute(self, a, b):
        result = CalculationCommand.divide(a, b)
        History.add_history('Divide', a, b, result)
        return result
    
class GetHistoryCommand(Command):
    def execute(self):
        return History.get_history()

class AddHistoryCommand(Command):
    def execute(self, record):
        operation, operand1, operand2, result = record.split(', ')
        History.add_history(operation, float(operand1), float(operand2), float(result))
        return "Added to history."

class DeleteHistoryCommand(Command):
    def execute(self):
        History.clear_history()
        return "History erased."
    