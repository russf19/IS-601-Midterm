from app.plugins.plugin.plugin import CommandPlugin

class HelloWorldCommand(CommandPlugin):
    def execute(self):
        return "Hello, World!"
    