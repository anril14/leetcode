from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i, item in enumerate(nums):
            new_arr.append(item)
        for i, item in enumerate(nums):
            new_arr.append(item)
        return new_arr

solution = Solution()
print(solution.getConcatenation([1,2,1]))
print(solution.getConcatenation([1,3,2,1]))