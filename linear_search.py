arr1 = [1, 4, 8, 25, 1101, 1400, 2100, 4001]


def linear_search(arr: list, target: int):
    iter_counter = 0
    for i, item in enumerate(arr):
        iter_counter += 1
        if item == target:
            return i, iter_counter
    return None, iter_counter


if __name__ == '__main__':
    result = linear_search(arr1, 1101)
    print(f'result: {result[0]} \niterations: {result[1]}')
