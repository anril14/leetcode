from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_arr = []
        sum = 0
        for i, item in enumerate(operations):
            match item:
                case 'C':
                    new_arr.pop()
                case 'D':
                    new_arr.append(int(new_arr[len(new_arr)-1])*2)
                case '+':
                    new_arr.append(int(new_arr[len(new_arr)-1])+int(new_arr[len(new_arr)-2]))
                case _:
                    new_arr.append(item)
        for i,item in enumerate(new_arr):
            sum += int(item)
        return sum

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))
print(solution.calPoints(["1","C"]))
