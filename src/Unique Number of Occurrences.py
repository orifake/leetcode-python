from typing import List
import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr).values()
        return len(set(cnt)) == len(cnt)


t = Solution()
print(t.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
