def binary_search(sorted_array, element):
    while len(sorted_array) > 0:
        print(sorted_array)
        index = (len(sorted_array) - 1) // 2
        if sorted_array[index] < element:
            sorted_array = sorted_array[(index+1):len(sorted_array)]
        elif sorted_array[index] > element:
            sorted_array = sorted_array[0:index]
        else:
            return sorted_array[index]

    return -1


def binary_search_recursion(sorted_array, element):
    print(sorted_array)
    index = (len(sorted_array)) // 2
    if element > sorted_array[index]:
        sorted_array = sorted_array[(index+1):len(sorted_array)]
        binary_search_recursion(sorted_array, element)
    elif element < sorted_array[index]:
        sorted_array = sorted_array[0:index]
        binary_search_recursion(sorted_array, element)
    else:
        return sorted_array[index]

    return -1


if __name__ == "__main__":
    arr = list(range(20))
    print(binary_search(arr, 17))
    print()
    print(binary_search(arr, 17))
