from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return -1


solution = Solution()
print(solution.search([1, 3, 3, 4, 5, 6, 7, 8], 1))
