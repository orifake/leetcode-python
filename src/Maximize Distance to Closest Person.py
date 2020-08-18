from typing import List
import itertools

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, int((K+1)/2))

        return max(ans, seats.index(1), seats[::-1].index(1))


t = Solution()
# print(t.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
# print(t.maxDistToClosest([1, 0, 0, 0]))
print(t.maxDistToClosest([0, 0, 1]))
