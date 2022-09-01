class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None

        result = self.head

        self.head = self.head.next_node

        return result

    def empty(self):
        if self.head:
            return False
        return True

    def printQueue(self):
        current_node = self.head
        printArray = []
        while current_node:
            printArray.append(current_node.data)
            current_node = current_node.next_node
        print(printArray)


if __name__ == "__main__":
    q = QueueLinkedList()

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
