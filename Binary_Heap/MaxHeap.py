from mimetypes import init


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self.size += 1
        self.__swap_up(self.size-1)

    def __swap_up(self, index: int) -> None:
        # if child > parent and index > 0
        if (self.heap[index] > self.heap[(index-1)//2]) and (index > 0):
            parent = self.heap[index]
            self.heap[index] = self.heap[(index-1)//2]
            self.heap[(index-1)//2] = parent

            self.__swap_up((index-1)//2)

    def get_max(self) -> int:
        return self.heap[0]

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def extract_max(self) -> int:
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heap.pop()
        self.__swap_down(0)
        return max_value

    def __swap_down(self, index: int) -> None:
        # if no left child return
        if (2*index)+1 > self.size-1:
            return
        # if 1st: no right child or 2nd: left > right
        if ((2*index)+2 > self.size-1) or (self.heap[(2*index)+1] > self.heap[(2*index)+2]):
            # if left > parent
            if self.heap[(2*index)+1] > self.heap[index]:
                temp = self.heap[index]
                self.heap[index] = self.heap[(2*index)+1]
                self.heap[(2*index)+1] = temp

                self.__swap_down((2*index)+1)
        # right >= left
        else:
            # if right > parent
            if self.heap[(2*index)+2] > self.heap[index]:
                temp = self.heap[index]
                self.heap[index] = self.heap[(2*index)+2]
                self.heap[(2*index)+2] = temp

                self.__swap_down((2*index)+2)

    def remove(self, index: int) -> None:
        self.heap[index] = self.heap[self.size-1]
        self.size -= 1
        self.heap.pop()
        self.__swap_down(index)

    def heapify(self, array: list) -> None:
        self.heap = array
        self.size = len(array)

        for i in range(self.size//2, -1, -1):
            self.__swap_down(i)

    def heap_sort(self, array: list) -> list:
        self.heapify(array)
        while self.size >= 1:
            temp = self.heap[0]
            self.heap[0] = self.heap[self.size-1]
            self.heap[self.size-1] = temp
            self.size -= 1
            self.__swap_down(0)
        return self.heap

    def printHeap(self):
        print(self.heap)


new_heap = MaxHeap()

for i in range(20):
    new_heap.insert(i)

new_heap.printHeap()

new_heap.heapify(list(range(20)))

new_heap.printHeap()

print(new_heap.extract_max())

new_heap.printHeap()

print(new_heap.extract_max())

new_heap.printHeap()

print(new_heap.extract_max())

new_heap.printHeap()

print(new_heap.heap_sort(list(range(19, -1, -1))))
