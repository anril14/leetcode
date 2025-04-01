class Solution:
    def climbStairs(self, n: int) -> int:
        two, one = 1, 1
        for _ in range(n - 1):
            one_temp = one
            one = two + one
            two = one_temp
        return one


solution = Solution()
print(solution.climbStairs(1))
