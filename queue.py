from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.q:
            return None
        return self.q.popleft()
