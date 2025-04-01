from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Counting each value in already sorted order
        count = [0, 0, 0]
        for i in nums:
            count[i] += 1

        i = 0
        for _ in range(len(count)):
            for j in range(count[_]):
                nums[i] = _
                i += 1


solution = Solution()
print(solution.sortColors([2, 0, 2, 1, 1, 0]))
