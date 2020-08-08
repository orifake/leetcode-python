from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)
        leftSum = 0
        for i, x in enumerate(nums):
            if leftSum == (Sum - leftSum - x):
                return i
            leftSum += x
        return -1


t = Solution()
print(t.pivotIndex([1, 7, 3, 6, 5, 6]))
