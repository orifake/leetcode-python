from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix, prefix = 0, 0
        for num in nums:
            prefix += num
            min_prefix = min(min_prefix, prefix)
        return 1 - min_prefix


t = Solution()
print(t.minStartValue([-3, 2, -3, 4, 2]))
