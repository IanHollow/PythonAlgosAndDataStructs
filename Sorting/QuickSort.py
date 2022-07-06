class QuickSort:
    def __init__(self, numbers: list):
        self.values = numbers

    def sort(self):
        self.quick_sort(0, len(self.values)-1)
        return self.values

    def quick_sort(self, left: int, right: int):
        if left == right:
            return

        split_index = self.partition(left, right)
        self.quick_sort(left, split_index-1)
        self.quick_sort(split_index, right)

    def partition(self, left: int, right: int) -> int:
        pivot = self.values[(left + right)//2]

        while left <= right:
            while self.values[left] < pivot:
                left += 1

            while self.values[right] > pivot:
                right -= 1

            if left <= right:
                temp = self.values[left]
                self.values[left] = self.values[right]
                self.values[right] = temp

                left += 1
                right -= 1

        return left


arr = [2, 5, 8, 2, 4, 5, 6, 6, 8, 1, 4, 5, 3, 5, 7, 7, 4, ]

sorted_list = QuickSort(arr)

print(sorted_list.sort())
