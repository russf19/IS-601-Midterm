from app.commands.command.command import Command
from app.plugins.history.history import History

class CalculationCommand(Command):

    @staticmethod
    # adds addition to calculator
    def add(a, b):
        result = a + b
        History.add_history(f"Added {a} to {b} got {result}")
        return result

    @staticmethod
    # adds subtraction operation to calculator
    def subtract(a, b):
        result = a - b
        History.add_history(f"Subtracted {a} from {b} got {result}")
        return result

    @staticmethod
    # adds multiplication operation to calculator
    def multiply(a, b):
        result = a * b
        History.add_history(f"Multiplied {a} by {b} got {result}")
        return result

    @staticmethod
    # adds division operation to calculator
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        History.add_history(f"Divided {a} by {b} got {result}")
        return result
    