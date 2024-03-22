import os
import importlib.util
import logging
import logging.config
from dotenv import load_dotenv
from app.commands.operation.operation import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, GetHistoryCommand, AddHistoryCommand, DeleteHistoryCommand
from app.plugins.plugin.plugin import CommandPlugin
from app.commands.exit.exit import ExitCommand
from app.commands.greet.greet import GreetCommand
from app.commands.goodbye.goodbye import GoodbyeCommand

class CalculatorApp:
    def __init__(self):
        self.commands = {}
        self.settings = {}
        self.load_dotenv()
        self.configure_logging()
        self.load_environment_variables()

    def load_dotenv(self):
        load_dotenv()

    def configure_logging(self):
        logging_conf_path = os.getenv('logging_conf_path', 'logging.conf')
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured")

    def load_environment_variables(self):
        self.settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")

    def load_plugins(self, directory):
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.py') and not filename.startswith('__'):
                    filepath = os.path.join(root, filename)
                    module_name = os.path.splitext(os.path.basename(filepath))[0]
                    spec = importlib.util.spec_from_file_location(module_name, filepath)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for attribute_name in dir(module):
                        attribute = getattr(module, attribute_name)
                        if isinstance(attribute, type) and issubclass(attribute, CommandPlugin):
                            command_instance = attribute()
                            command_key = command_instance.__class__.__name__.lower().replace('command', '')
                            self.commands[command_key] = command_instance
        return self

    def add_static_commands(self):
        self.commands.update({
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
            'greet': GreetCommand(),
            'goodbye': GoodbyeCommand(),
            'exit': ExitCommand(),
            'get_history': GetHistoryCommand(),
            'add_history': AddHistoryCommand(),
            'delete_history': DeleteHistoryCommand()
        })
        return self

    def get_command(self, command_name_str):
        return self.commands.get(command_name_str)

    def build(self):
        return self

def menu(commands):
    print("\nAvailable Commands:")
    for command in sorted(commands.keys()):
        print(f" - {command}")
    print("Type 'exit' to close the calculator.\n")

def main():
    app = CalculatorApp().load_plugins(os.path.join('app', 'plugins')).add_static_commands().build()

    logging.info("Welcome to my calculator! To get started, type a command and numbers. If you want to exit, type 'exit'.")
    print("Welcome to my calculator! To get started, type a command and numbers. If you want to exit, type 'exit'.")

    first_run = True

    while True:
        if first_run:
            menu(app.commands)
            first_run = False
        
        command_input = input("Enter a command: ").strip().lower()
        if not command_input:
            continue

        command_parts = command_input.split()
        command_name = command_parts[0].strip().lower()
        command = app.get_command(command_name)

        if not command:
            print("Error. This is not a valid command.")
            continue

        # Handling commands with two arguments (basic arithmatic operations +, -, *, /)
        if command_name in ['add', 'subtract', 'multiply', 'divide'] and len(command_parts) == 3:
            try:
                num1, num2 = map(float, command_parts[1:])
                result = command.execute(num1, num2)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid numbers.")
            except Exception as e:
                print(f"Error: {e}")

        # Handling commands without additional arguments (helloworld)
        elif len(command_parts) == 1:
            try:
                print(command.execute())
            except Exception as e:
                print(f"Error: {e}")

        # Handling commands like 'add_history' which require additional arguments beyond the command name
        elif command_name in ['add_history', 'delete_history'] and len(command_parts) > 1:
            record = " ".join(command_parts[1:])
            try:
                print(command.execute(record))
            except Exception as e:
                print(f"Error: {e}")

        # Handling 'get_history' which does not require additional arguments
        elif command_name == 'get_history':
            try:
                print(command.execute())
            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
