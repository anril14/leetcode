from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = dict()
        for i in nums:
            if i not in elements:
                elements.update({i: 1})
            else:
                elements[i] += 1
        highest_key = max(elements, key=elements.get)
        return highest_key


solution = Solution()
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
