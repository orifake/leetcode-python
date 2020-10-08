from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(1, n)]+[-n*(n-1)//2]


t = Solution()
print(t.sumZero(5))
