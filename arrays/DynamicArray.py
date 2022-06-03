import ctypes


class DynamicArray:

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = self._make_array(self.capacity)

    def __len__(self):
        return self.size

    def capacity(self):
        return self.capacity

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def get(self, index):
        if index < 0 or index >= self.size:
            return IndexError('Index out of Bounds')

        return self.arr[index]

    def push(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.arr[self.size] = element
        self.size += 1

    def insert(self, index, element):
        if index < 0 or index >= self.size:
            return IndexError('Enter an Appropiate Index')

        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.size-1, index-1, -1):
            self.arr[i+1] = self.arr[i]

        self.arr[index] = element
        self.size += 1

    def prepend(self, element):
        self.insert(0, element)

    def pop(self):
        if self.size == 0:
            print('Array is Empty Cannot Remove Last Element')
            return

        element = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1

        return element

    def removeAt(self, index):
        if self.size == 0:
            print('Array is Empty Cannot Remove Last Element')
            return

        if index == self.size-1:
            self.arr[index] = None
            self.size -= 1
            return

        if index < 0 or index >= self.size:
            return IndexError('Index out of Bounds')

        for i in range(index, self.size-1):
            self.arr[i] = self.arr[i+1]

        self.arr[self.size-1] = None
        self.size -= 1

    def find(self, element):
        for i in range(len(self.arr)):
            if self.arr[i] == element:
                return i
        return -1

    def _resize(self, new_capacity):
        BiggerArray = self._make_array(new_capacity)

        for i in range(self.size):
            BiggerArray[i] = self.arr[i]

        self.arr = BiggerArray
        self.capacity = new_capacity

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


arr = DynamicArray()

arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.push(5)

print(arr)

print(len(arr))

print(arr.is_empty())

print(arr.get(1))

arr.insert(2, 9)

print(arr)

arr.prepend(0)

print(arr)

arr.pop()

print(arr)

arr.removeAt(1)

print(arr)

print(arr.find(9))
