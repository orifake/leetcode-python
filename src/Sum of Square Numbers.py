import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 1 or c == 0:
            return True

        for i in range(1, c):
            if c - i * i < 0:
                return False
            rest = math.sqrt(c - i * i)
            if int(rest) == rest:
                return True

        return False


t = Solution()
print(t.judgeSquareSum(5))
