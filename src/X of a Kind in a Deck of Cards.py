from typing import List
from math import gcd
from functools import reduce
import collections

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = collections.Counter(deck).values()
        print(vals)
        return reduce(gcd, vals) >= 2

t = Solution()
print(t.hasGroupsSizeX([1,2,3,4,4,3,2,1]))