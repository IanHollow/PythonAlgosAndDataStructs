from locale import currency


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedListWithTail:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return True
        return False

    def value_at(self, index):
        if index < 0 or index >= self.size:
            return IndexError('Index out of Bounds')

        current_node = self.head
        i = 0
        while i <= index:
            current_node = self.head.next_node
            i += 1
        return current_node.data

    def push_front(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next_node = self.head
            self.head = new_node.next_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def pop_front(self):
        if not self.head:
            print('List is empty cannot remove first value')
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
        if not self.tail:
            print('List is empty cannot remove last value')
            return

        current_node = self.head
        while current_node.next_node != self.tail:
            current_node = current_node.next_node

        result = self.tail.data
        self.tail = current_node
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

        i = 0
        while i < index:
            current_node = current_node.next_node
            i += 1

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def erase(self, index):
        current_node = self.head

        if index == 0:
            self.pop_front()
            return

        if (index + 1) == self.size:
            self.pop_back()
            return

        i = 0
        while i < index:
            current_node = current_node.next_node
            i += 1
        self.size -= 1

        current_node.next_node = (current_node.next_node).next_node

    def value_n_from_end(self, index):
        value = 0
        current_node = self.head
        i = 0
        while i < index:
            current_node = current_node.next_node
            i += 1

        while current_node:
            current_node = current_node.next_node
            value += 1

        return value

    def reverse(self):
        for i in range(self.size):
            self.push_back(self.pop_front())
            
    def remove_value(self, value):
        current_node = self.head

        i = 0
        while current_node:
            if current_node.data == value:
                self.erase(i)
                return
            current_node = current_node.next_node
            i += 1
            
        print('List does not have value specified')    
        return
