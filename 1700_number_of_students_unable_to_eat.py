from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1=0
        s0=0
        for i, item in enumerate(students):
            s1 = s1 + 1 if item == 1 else s1 + 0
            s0 = s0 + 1 if item == 0 else s0 + 0
        for s in sandwiches:
            if s == 0:
                if s0 > 0:
                    s0 -= 1
                else:
                    return s1 + s0
            elif s == 1:
                if s1 > 0:
                    s1 -= 1
                else:
                    return s1 + s0
        return s1 + s0

solution = Solution()
print(solution.countStudents([1,1,0,0], [0,1,0,1]))
print(solution.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))