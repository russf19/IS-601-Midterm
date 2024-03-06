from app.commands.command.command import Command
import logging

class test():
    myval = 10
    yourval = 11

class GreetCommand(Command):
    def execute(self):
        logging.info("Hello World!")

        mydict = {1,2,3,4,5}
        logging.debug(print(test))

        print("Hello, World!")
    