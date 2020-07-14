from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s = sum(nums)
        m = min(nums)
        return s - len(nums) * m


t = Solution()
print(t.minMoves([1, 2, 3]))
