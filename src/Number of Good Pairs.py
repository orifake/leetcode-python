from typing import List
import collections


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        count = collections.Counter(nums)
        for i in count:
            if count[i] > 1:
                ans += int((count[i] * (count[i] - 1)) / 2)
        return ans


t = Solution()
print(t.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
