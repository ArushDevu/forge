class DependencyGraph:
    def __init__(self, tasks):
        self.tasks = tasks

    def resolve(self):
        order = []
        finished = set()
        
        while len(order) < len(self.tasks):
            for task in self.tasks:
                if task.name in finished:
                    continue

                if all(dependency in finished for dependency in task.dependencies):
                    order.append(task.name)
                    finished.add(task.name)

        return order