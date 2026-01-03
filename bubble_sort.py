arr1 = [4, 8, 25, 1, 0, 1400, 4001, 2100]
arr2 = [5, 6, 1, 3]


def bubble_sort(arr: list):
    iter_counter = 0

    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                iter_counter += 1

                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr, iter_counter


if __name__ == '__main__':
    result = bubble_sort(arr1)
    print(f'result: {result[0]} \niterations: {result[1]}')
