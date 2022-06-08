class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def empty(self):
        if self.head:
            return False
        return True

    def value_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of Bounds")

        current_node = self.head

        for _ in range(index):
            current_node = self.head.next_node

        return current_node.data

    def push_front(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next_node = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def pop_front(self):
        if not self.head:
            print("List is empty cannot remove first value")
            return

        result = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        return result

    def push_back(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def pop_back(self):
        if not self.head:
            print("List is empty cannot remove last value")
            return

        current_node = self.head
        while current_node.next_node.next_node:
            current_node = current_node.next_node
        result = self.tail.data
        self.tail = current_node
        self.tail.next_node = None
        self.size -= 1
        return result

    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data

    def insert(self, index, data):
        new_node = Node(data)
        current_node = self.head

        if index == 0:
            self.push_front(data)
            return

        if (index + 1) == self.size:
            self.push_back(data)
            return

        for _ in range(index-1):
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        self.size += 1

    def erase(self, index):
        current_node = self.head

        if index == 0:
            self.pop_front()
            return

        if (index + 1) == self.size:
            self.pop_back()
            return

        for _ in range(index-1):
            current_node = current_node.next_node

        current_node.next_node = current_node.next_node.next_node

        self.size -= 1

    def value_n_from_end(self, index):
        value = 0
        current_node = self.head

        if index < 0 or index >= self.size:
            raise IndexError("Index out of Bounds")

        i = 0
        while i < index:
            current_node = current_node.next_node
            i += 1

        while current_node:
            current_node = current_node.next_node
            value += 1

        return value

    def reverse(self):
        if not self.head:
            print("List is empty cannot reverse")
            return

        temp_tail = self.tail
        while temp_tail != self.head:
            front_node = self.head
            self.head = self.head.next_node

            front_node.next_node = temp_tail.next_node
            temp_tail.next_node = front_node

            if not front_node.next_node:
                self.tail = front_node

    def remove_value(self, value):
        current_node = self.head

        i = 0
        while current_node:
            if current_node.data == value:
                self.erase(i)
                return
            current_node = current_node.next_node
            i += 1

        print("List does not have value specified")

    def printList(self):
        current_node = self.head
        printArray = []
        while current_node:
            printArray.append(current_node.data)
            current_node = current_node.next_node
        print(printArray)


if __name__ == "__main__":
    listLink = LinkedListWithTail()

    listLink.push_front(1)
    listLink.push_front(2)
    listLink.push_front(3)
    listLink.push_front(4)
    listLink.push_front(5)

    listLink.printList()

    listLink.pop_front()
    listLink.pop_back()

    listLink.printList()

    listLink.insert(1, 7)
    listLink.remove_value(2)

    listLink.printList()

    listLink.push_back(5)

    listLink.printList()

    listLink.reverse()

    print(len(listLink))

    listLink.printList()

    print(listLink.back())

    print(listLink.empty())

    print(listLink.value_at(1))

    listLink.erase(1)

    listLink.printList()

    print(listLink.value_n_from_end(2))
