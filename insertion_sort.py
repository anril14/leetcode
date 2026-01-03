arr1 = [2, 3, 4, 1, 6]


def insertion_sort(arr: list):
    iter_counter = 0

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            iter_counter += 1

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr, iter_counter


if __name__ == '__main__':
    result = insertion_sort(arr1)
    print(f'result: {result[0]} \niterations: {result[1]}')
