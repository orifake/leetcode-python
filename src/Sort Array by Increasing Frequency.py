from typing import List
import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))


t = Solution()
print(t.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
