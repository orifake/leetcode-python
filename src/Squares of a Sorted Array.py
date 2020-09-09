from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x * x for x in A)


t = Solution()
print(t.sortedSquares([-7, -3, 2, 3, 11]))
