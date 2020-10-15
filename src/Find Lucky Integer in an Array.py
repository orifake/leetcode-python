from typing import List
import collections


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = [-1]
        count = collections.Counter(arr)
        for i in count:
            if i == count[i]:
                ans.append(i)
        return max(ans)


t = Solution()
print(t.findLucky([2, 2, 3, 4]))
