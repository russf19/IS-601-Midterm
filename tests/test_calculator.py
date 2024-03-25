import pytest
from app.plugins.calculation.calculation import CalculationCommand
from app.plugins.history.history import History
from app.plugins.greet.greet import GreetCommand
from app.plugins.goodbye.goodbye import GoodbyeCommand
from app.plugins.exit.exit import ExitCommand
from app.plugins.hello_world.helloworld_command import HelloWorldCommand

def test_add():
    #Tests to see if addition works
    calc = CalculationCommand()
    assert calc.add(1, 2) == 3

def test_subtract():
    #Tests to see if subtraction works
    calc = CalculationCommand()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    #Tests to see if multiplication works
    calc = CalculationCommand()
    assert calc.multiply(2, 4) == 8

def test_divide():
    #Tests to see if division works
    calc = CalculationCommand()
    assert calc.divide(8, 2) == 4

def test_divide_by_zero():
    #Tests to see if dividing by zero runs or fails
    with pytest.raises(ZeroDivisionError):
        CalculationCommand.divide(1, 0)

def test_history():
    History.clear_history()
    CalculationCommand.add(10, 20)
    history_output = History.get_history()
    # Defines the expected output based on the format of the history DataFrame's string representation
    expected_output_part = "Add    10.0    20.0    30.0"
    # Check to see if the expected part is in the history output
    assert expected_output_part in history_output, f"Expected '{expected_output_part}' to be in history, but it wasn't. History output: '{history_output}'"

def test_greet():
    #Tests to see if greet command works
    greet = GreetCommand()
    assert greet.execute() == "Welcome to my calculator! To get started type a command and numbers. If you want to exit, type 'exit'."

def test_goodbye():
    #Tests to see if goodbye command works
    goodbye = GoodbyeCommand()
    assert goodbye.execute() == "Goodbye."

def test_exit():
    #Tests to see if exit command works
    exit_command = ExitCommand()
    with pytest.raises(SystemExit):
        exit_command.execute()

def test_helloworld():
    #Tests to see if helloworld command works
    hello_world = HelloWorldCommand()
    assert hello_world.execute() == "Hello, World!"
