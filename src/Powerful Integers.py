from typing import List
import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = []
        xn = 1 if x == 1 else int(math.log(bound, x) + 1)
        yn = 1 if y == 1 else int(math.log(bound, y) + 1)

        for ix in range(0, xn):
            for iy in range(0, yn):
                r = x**ix + y**iy
                if r <= bound and r not in ans:
                    ans.append(r)
        return ans


t = Solution()
print(t.powerfulIntegers(1, 2, 1000000))
