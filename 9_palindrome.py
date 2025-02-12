from math import ceil, floor

class Solution:
    def is_palindrome(self, x: int) -> bool:
        if str(x)[:floor(len(str(x))/2)] == str(x)[:ceil(len(str(x))/2)-1:-1]:
            return True
        else:
            return False


solution = Solution()
print(solution.is_palindrome(12321))
