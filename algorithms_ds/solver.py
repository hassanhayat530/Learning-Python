def solve(start, goal, neigh_fn, state_eq, state_key):

    class Node:
        def __init__(self, val, prev):
            self.val = val
            self.prev = prev

    class Queue:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return len(self.items) == 0

        def enqueue(self, node):
            self.items.append(node)

        def dequeue(self):
            assert not self.is_empty(), 'queue is empty'
            return self.items.pop(0)

    visited = []
    q = Queue()
    q.enqueue(Node(start, None))
    visited.append(start)

    while not q.is_empty():
        current_node = q.dequeue()
        current_state = current_node.val

        if state_eq(current_state, goal):
            path = []
            while current_node is not None:
                path.append(current_node.val)
                current_node = current_node.prev
            return list(reversed(path))

        for neighbor in neigh_fn(current_state):
            if neighbor not in visited:
                visited.append(neighbor)
                neighbor_node = Node(neighbor, current_node)
                neighbor_node.prev = current_node
                q.enqueue(neighbor_node)

    return None

