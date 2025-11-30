class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)


# Depth-First Iterator
class DepthFirstIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        self.stack.extend(reversed(node.children))
        return node.value


# Breadth-First Iterator
class BreadthFirstIterator:
    def __init__(self, root):
        self.queue = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration
        node = self.queue.pop(0)
        self.queue.extend(node.children)
        return node.value

root = Node("A")
root.add_child(Node("B"))
root.add_child(Node("C"))
root.children[0].add_child(Node("D"))
root.children[0].add_child(Node("E"))

print("Depth-First:")
for val in DepthFirstIterator(root):
    print(val)

print("\nBreadth-First:")
for val in BreadthFirstIterator(root):
    print(val)
