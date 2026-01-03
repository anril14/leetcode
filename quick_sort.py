arr1 = [4, 8, 25, 1, 0, 1400, 4001, 2100]

iter_counter = 0


def quick_sort(arr: list):
    global iter_counter

    if len(arr) <= 1:
        return arr

    pivot = len(arr) // 2

    left = []
    right = []

    for i in arr:
        if i == arr[pivot]:
            continue

        iter_counter += 1
        if i < arr[pivot]:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [arr[pivot]] + quick_sort(right)


if __name__ == '__main__':
    result = quick_sort(arr1)
    print(f'result: {result} \niterations: {iter_counter}')
