from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sub = []
        for i in range(n):
            sub.append(nums[i])
            sub.append(nums[i + n])
        return sub

solution = Solution()
print(solution.shuffle([2,5,1,3,4,7], 3))
print(solution.shuffle([1,2,3,4,4,3,2,1], 4))
print(solution.shuffle([1,1,2,2], 2))
