from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        index = 0
        for i, num in enumerate(nums):
            if num == m:
                index = i
            if num != m and m < 2 * num:
                return -1
        return index


t = Solution()
print(t.dominantIndex([3, 6, 1, 0]))