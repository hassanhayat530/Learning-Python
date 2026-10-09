class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = self.size * [None]
        self.head = self.tail = 0
        self.count_items = 0
        self.sum = 0

    def enqueue(self, n):
        self.sum += n
        self.queue[self.tail] = n
        self.tail = (self.tail + 1) % len(self.queue)
        self.count_items += 1
        if self.count_items == self.size:
            self.resize()

    def dequeue(self):
        x = self.queue[self.head]
        self.sum -= x
        self.queue[self.head] = None
        self.head = (self.head + 1) % len(self.queue)
        self.count_items -= 1
        return x

    def count(self):
        return self.count_items

    def avg(self):
        return self.sum / self.count()

    def resize(self):
        new_size = len(self.queue) * 2
        new_queue = [None] * new_size
        for i in range(self.count()):
            new_queue[i] = self.queue[(self.head + i) % self.size]
        self.head = 0
        self.tail = self.size
        self.size = new_size
        self.queue = new_queue
        print('Resized to' ,new_size, 'elements')
