import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n:
            result += math.floor(n / 5)
            n = math.floor(n / 5)

        return result

t = Solution()
print(t.trailingZeroes(5))