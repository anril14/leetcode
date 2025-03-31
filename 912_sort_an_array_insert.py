from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        for j in range(1, len(nums)):
            i = j-1
            print('i', i, 'j', j)
            print(nums[i], nums[j])
            while i>=0 and nums[i]>nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i -= 1
                j -= 1

        return nums


solution = Solution()
solution.sortArray([5,3,25,1])