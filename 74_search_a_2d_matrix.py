from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            low, high = 0, len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                if target < arr[mid]:
                    high = mid - 1
                elif target > arr[mid]:
                    low = mid + 1
                else:
                    return True
        return False


solution = Solution()
print(solution.searchMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
