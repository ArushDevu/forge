from forge.task import Task
from forge.graph import DependencyGraph


def test_graph_stores_tasks():
    a = Task("A", "echo A", [])
    b = Task("B", "echo B", ["A"])

    graph = DependencyGraph([a, b])

    assert graph.tasks[0].name == "A"
    assert graph.tasks[1].name == "B"


def test_graph_resolves_dependencies():
    a = Task("A", "echo A", [])
    b = Task("B", "echo B", ["A"])
    c = Task("C", "echo C", ["A"])
    d = Task("D", "echo D", ["B", "C"])

    graph = DependencyGraph([a, b, c, d])

    order = graph.resolve()

    assert order.index("A") < order.index("B")
    assert order.index("A") < order.index("C")
    assert order.index("B") < order.index("D")
    assert order.index("C") < order.index("D")