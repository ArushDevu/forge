class Task:
    def __init__(self, name, command, dependencies):
        self.name = name
        self.command = command
        self.dependencies = dependencies
        