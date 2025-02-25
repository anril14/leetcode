class Kadane:
    def bruteForce(self, nums: list):
        """O(n**2) time"""

        maxSum = nums[0]
        for i in range(len(nums)):
            curSum = 0
            for j in range(i,len(nums)):
                curSum += nums[j]
                maxSum = max(maxSum, curSum)
        return maxSum

    def kadanes(self, nums: list):
        """O(n) time"""

        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum

    def slidingWindow(self, nums):
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0
        L = 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R

            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R
        return maxL, maxR

solution = Kadane()
print(solution.kadanes( [4, -1, 2, -7, 3, 4] ))
print(solution.slidingWindow( [4, -1, 2, -7, 3, 4] ))
