from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        right = nums[-3] * nums[-2] * nums[-1]
        left = nums[0] * nums[1] * nums[-1]
        return max(right, left)


t = Solution()
print(t.maximumProduct([1, 2, 3, 4]))
