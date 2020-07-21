from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        c = Counter(nums)
        if k == 0:
            return len([i for i in c if c[i] > 1])

        if k > 0:
            return sum([i + k in c for i in c])


t = Solution()
print(t.findPairs([1, 2, 3, 4, 5], 1))
