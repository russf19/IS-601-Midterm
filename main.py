import os
import importlib.util
import logging
import logging.config
from dotenv import load_dotenv
from app.commands.operation.operation import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, GetHistoryCommand, AddHistoryCommand, DeleteHistoryCommand, Command
from app.commands.exit.exit import ExitCommand
from app.commands.greet.greet import GreetCommand
from app.commands.goodbye.goodbye import GoodbyeCommand

#Loading environment variables
load_dotenv()

def configure_logging():
    logging_conf_path = os.getenv('logging_conf_path', 'logging.conf')
    if os.path.exists(logging_conf_path):
        logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging configured")

def load_environment_variables():
    settings = {key: value for key, value in os.environ.items()}
    logging.info("Environment variables loaded.")
    return settings

def get_environemtn_variable(settings, env_var: str = 'ENVIRONMENT'):
    return settings.get(env_var, None)

PLUGIN_DIR = 'app/plugins'
def load_plugins():
    plugins = {}
    for filename in os.listdir(PLUGIN_DIR):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            path = os.path.join(PLUGIN_DIR, filename)
            module_spec = importlib.util.spec_from_file_location(module_name, path)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)            
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if issubclass(attribute, Command) and attribute is not Command:
                    # Assuming each command class has a unique name
                    plugins[attribute_name.lower()] = attribute()
    return plugins

settings = load_environment_variables()

def get_command(command_name_str):
    commands_dict = {
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
    }
    return commands_dict.get(command_name_str)

#Load environment variables

def main():
    configure_logging()
    
    logging.info("Welcome to my calculator! To get started type a command and numbers. If you want to exit, type 'exit'.")
    print("Welcome to my calculator! To get started type a command and numbers. If you want to exit, type 'exit'.")

    while True:
        command_input = input("Please enter a command: ").strip().lower()
        if not command_input:
            continue

        command_parts = command_input.split()
        command_name = command_parts[0]
        command = get_command(command_name)

        if not command:
            print("Error. This is not a valid command.")
            continue

        if command_name in ['add', 'subtract', 'multiply', 'divide'] and len(command_parts) == 3:
            try:
                num1, num2 = map(float, command_parts[1:])
                result = command.execute(num1, num2)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid numbers.")
            except Exception as e:
                print(f"Error: {e}")
        elif command_name in ['greet', 'goodbye', 'exit']:
            print(command.execute())
        elif command_name == 'add_history' and len(command_parts) > 1:
            record = " ".join(command_parts[1:])
            print(command.execute(record))
        elif command_name in ['get_history', 'delete_history']:
            print(command.execute())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
