class DependencyGraph:
    def __init__(self, tasks):
        self.tasks = tasks

    def resolve(self):
        order = []