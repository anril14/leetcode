from typing import List


def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    i = 0
    j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


class Solution:
    def sortArray(self, nums: List[int], **kwargs) -> List[int]:
        start = kwargs.get('start', 0)
        end = kwargs.get('end', len(nums) - 1)
        if end - start + 1 <= 1:
            return nums

        mid = (start + end) // 2

        self.sortArray(nums, start=start, end=mid)
        self.sortArray(nums, start=mid + 1, end=end)

        merge(nums, start, mid, end)

        return nums


solution = Solution()
print(solution.sortArray([5, 3, 25, 1]))
