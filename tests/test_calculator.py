import pytest
from app.commands.calculation.calculation import CalculationCommand
from app.commands.history.history import History
from app.commands.greet.greet import GreetCommand
from app.commands.goodbye.goodbye import GoodbyeCommand

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
    #Tests retrieving hprevious calculations
    History.clear_history()
    CalculationCommand.add(10, 20)
    assert "Added 10 to 20 got 30" in History.get_history()

def test_greet():
    #Tests to see if greet command works
    greet = GreetCommand()
    assert greet.execute() == "Welcome to my calculator! To get started type a command and numbers. If you want to exit, type 'exit'."

def test_goodbye():
    #Tests to see if goodbye command works
    goodbye = GoodbyeCommand()
    assert goodbye.execute() == "Goodbye."
