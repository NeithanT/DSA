

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] > target:
            right = middle
        if arr[middle] < target:
            left = middle + 1
        else:
            return middle
        
    return -1

def binary_search_rotated(arr, target):
    pass

def binary_search_rotated_minimum(arr):
    pass

if __name__ == "__main__":


    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    rotated_arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]

    target = 5

    print("Binary Search:", binary_search(arr, target))
    print("Binary Search Rotated:", binary_search_rotated(rotated_arr, target))
    print("Binary Search Rotated Minimum:", binary_search_rotated_minimum(rotated_arr))