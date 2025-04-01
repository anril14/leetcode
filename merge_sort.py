def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    i = 0
    j = 0
    k = start

    # Firstly if we can increment both
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Secondly if only once (keep in mind that these are cycles)
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr: list, **kwargs):
    start = kwargs.get('start', 0)
    end = kwargs.get('end', len(arr) - 1)
    if end - start + 1 <= 1:
        return arr

    mid = (start + end) // 2

    # New "left" recursion branch and sorting it
    merge_sort(arr, start=start, end=mid)

    # New "right" recursion branch and sorting it
    merge_sort(arr, start=mid + 1, end=end)

    # Merging everything
    merge(arr, start, mid, end)

    return arr


print(merge_sort([5, 4, 3, 2, 1]))
