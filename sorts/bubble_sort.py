def bubble_sort(arr):
    swapped = False
    j = 0
    for j in range(len(arr)):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr

arr = [2, 5, 1, 6, 3, 4]
print(bubble_sort(arr))
arr = [0, 1, 2, 3]
print(bubble_sort(arr))