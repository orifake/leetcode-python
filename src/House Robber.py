from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now


t = Solution()
print(t.rob([2, 7, 9, 3, 1]))
