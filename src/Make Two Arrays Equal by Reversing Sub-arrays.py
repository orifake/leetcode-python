from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort(), arr.sort()
        return target == arr


t = Solution()
print(t.canBeEqual([3, 7, 9], [3, 7, 11]))
