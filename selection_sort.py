arr1 = [4, 8, 25, 1, 0, 1400, 4001, 2100]


def selection_sort(arr: list):
    iter_counter = 0

    for i in range(0, len(arr) - 1):
        index_min = i

        for j in range(i + 1, len(arr)):
            iter_counter += 1
            if arr[j] < arr[index_min]:
                index_min = j

        if index_min != i:
            temp = arr[i]
            arr[i] = arr[index_min]
            arr[index_min] = temp

    return arr, iter_counter


if __name__ == '__main__':
    result = selection_sort(arr1)
    print(f'result: {result[0]} \niterations: {result[1]}')
