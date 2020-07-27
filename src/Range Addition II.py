from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x = m
        y = n
        for i in range(0,len(ops)):
            x = min(x,ops[i][0])
            y = min(y,ops[i][1])

        return x * y

t =Solution()
print(t.maxCount(3,3,[[2,2],[3,3]]))