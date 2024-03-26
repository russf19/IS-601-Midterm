import os
import importlib.util
import logging
import logging.config
from dotenv import load_dotenv
from app.commands.command.command import Command

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

    def load_commands(self, directory):
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
                        if isinstance(attribute, type) and issubclass(attribute, Command):
                            command_instance = attribute()
                            command_key = command_instance.__class__.__name__.lower().replace('command', '')
                            self.commands[command_key] = command_instance
        return self

    def get_command(self, command_name_str):
        return self.commands.get(command_name_str)

    def build(self):
        return self

def menu(commands):
    print("\nMy Calculator Commands:")
    # exclude these commands
    exclude_commands = ['calculation', '']
    for command in sorted(commands.keys()):
        # Only displays the commands if they are not in the exclude list
        if command not in exclude_commands:
            print(f" - {command}")
    print("Type 'exit' to close the calculator.\n")

# Executes the calculator app and starts the loop.
def main():
    app = CalculatorApp().load_commands(os.path.join('app', 'commands')).load_commands(os.path.join('app', 'plugins')).build()

    logging.info("Welcome to my calculator! To get started, type a command and numbers. If you want to exit, type 'exit'.")
    print("Welcome to my calculator! To get started, type a command and numbers. If you want to exit, type 'exit'.")

# Checks to see if calculator is first starting up and sets a flag. Menu only shows at the beginning. Then after executing a command, checks for the flag. Stops displaying the menu after flag is set.
    first_run = True

    while True:
        if first_run:
            menu(app.commands)
            first_run = False

        command_input = input("Enter a command: ").strip().lower()
        logging.warning(f"Warning: Not a command.")
        if not command_input:
            continue

        command_parts = command_input.split()
        command_name = command_parts[0].strip().lower()
        command = app.get_command(command_name)

        if not command:
            logging.error(f"Invalid commmand entered: {command_name}")
            print("Error. This is not a valid command.")
            continue

        try:
            if command_name in ['add', 'subtract', 'multiply', 'divide'] and len(command_parts) == 3:
                num1, num2 = map(float, command_parts[1:])
                result = command.execute(num1, num2)
                print(f"Result: {result}")
            elif len(command_parts) >= 1:
                result = command.execute(*command_parts[1:])
                print(result if result is not None else "Command executed successfully.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
