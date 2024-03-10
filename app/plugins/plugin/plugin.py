#Master command class thats sets the structure of all plugins

class CommandPlugin:
    def execute(self):
        raise NotImplementedError("Execute method not implemented")
    