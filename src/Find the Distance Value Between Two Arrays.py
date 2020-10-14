from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int],
                             d: int) -> int:
        return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)


t = Solution()
print(t.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
