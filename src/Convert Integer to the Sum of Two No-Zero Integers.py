from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]


t = Solution()
print(t.getNoZeroIntegers(1010))
