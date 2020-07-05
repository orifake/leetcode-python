import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return (math.log10(num) / math.log10(4)) % 1 == 0


t = Solution()
print(t.isPowerOfFour(4))