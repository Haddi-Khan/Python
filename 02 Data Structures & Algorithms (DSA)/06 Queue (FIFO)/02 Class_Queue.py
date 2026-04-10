from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.q:
            return "Queue Underflow"
        return self.q.popleft()

    def front(self):
        if not self.q:
            return "Queue is empty"
        return self.q[0]

    def is_empty(self):
        return len(self.q) == 0

q = Queue()
q.enqueue(5)
q.enqueue(15)
q.enqueue(25)
print(q.dequeue())
print(q.front())
