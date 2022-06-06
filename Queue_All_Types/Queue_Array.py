class QueueArray:
    def __init__(self, capacity):
        self.queue = [None]*capacity
        self.front = self.rear = self.size = 0
        self.capacity = capacity

    def full(self):
        if self.size == self.capacity:
            return True
        return False

    def empty(self):
        if self.size == 0:
            return True
        return False

    def enqueue(self, value):
        if self.full():
            print('Queue Full')
            return

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity

        self.size += 1

    def dequeue(self):
        if self.empty():
            print('Queue Empty')
            return

        value = self.queue[self.front]

        self.queue[self.front] = None
        self.size -= 1

        self.front = (self.front + 1) % self.capacity

        return value

    def printQueue(self):
        print(self.queue)


if __name__ == '__main__':
    q = QueueArray(4)

    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)

    q.printQueue()

    q.dequeue()

    q.dequeue()

    q.printQueue()

    q.enqueue(100)

    q.printQueue()

    q.enqueue(500)

    q.printQueue()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(303)

    q.printQueue()
