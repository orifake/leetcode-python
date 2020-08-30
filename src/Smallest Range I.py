from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxA = max(A)
        minA = min(A)
        return max(0, maxA - minA - 2 * K)


t = Solution()
print(t.smallestRangeI([1, 3, 6], 3))
