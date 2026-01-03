from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            # print(f'left {left}, mid {mid}, right {right}')

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        else:
            return left


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 1))
