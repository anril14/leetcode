from typing import List, Optional

class Solution:
    def two_sum(self, nums: List[int], target: int) -> Optional[List[int]]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[nums[i]] = i
        return None

solution = Solution()
print(solution.two_sum([1,2,3],3))
