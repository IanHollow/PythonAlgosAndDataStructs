class MergeSort():
    def __init__(self, numbers: list):
        self.values = numbers
        self.count = len(numbers)

    def sort(self) -> list:
        self.merge_sort(0, self.count-1)
        return self.values

    def merge_sort(self, low: int, high: int) -> None:
        if low < high:
            mid = (low + high)//2

            self.merge_sort(low, mid)
            self.merge_sort(mid+1, high)
            self.merge(low, mid, high)

    def merge(self, low: int, mid: int, high: int) -> list:
        result = []
        i = low
        j = mid+1

        while i <= mid and j <= high:
            if self.values[i] < self.values[j]:
                result.append(self.values[i])
                i += 1
            elif self.values[i] > self.values[j]:
                result.append(self.values[j])
                j += 1
            else:
                if i <= j:
                    result.append(self.values[i])
                    i += 1
                else:
                    result.append(self.values[i])
                    j += 1

        while i <= mid:
            result.append(self.values[i])
            i += 1

        while j <= high:
            result.append(self.values[i])
            j += 1

        for index in range(len(result)):
            self.values[low + index] = result[index]


arr = [2, 5, 8, 2, 4, 5, 6, 6, 8, 1, 4, 5, 3, 5, 7, 7, 4, ]

merged_list = MergeSort(arr)

print(merged_list.sort())
