from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        new_list = []
        for i in range(len(nums)):
            if nums[i] != val:
                new_list.append(nums[i])
                k += 1
        for i in range(len(new_list)):
            nums[i] = new_list[i]
        return k

solution = Solution()
print(solution.removeElement([3,2,2,3], 3))
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))