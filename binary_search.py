import math

# только если массив упорядоченный!
arr1 = [1, 3, 3, 4, 5, 6, 7, 8]


def binary_search(arr: list, target: int):
    iter_counter = 0
    if len(arr) == 0:
        return None, iter_counter

    left = 0
    right = len(arr) - 1

    while left <= right:

        iter_counter += 1

        mid = (left + right) // 2

        guess = arr[mid]
        if guess == target:
            return mid, iter_counter

        if target < guess:
            right = mid - 1
        else:
            left = mid + 1
    return None, iter_counter


if __name__ == '__main__':
    result = binary_search(arr1, 3)
    print(f'result: {result[0]} \niterations: {result[1]}')
