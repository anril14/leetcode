def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j -= 1
    return arr

print(insertion_sort([2,3,4,1,6]))
