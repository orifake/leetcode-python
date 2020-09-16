from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int,
                          c0: int) -> List[List[int]]:
        dis = []
        for r in range(R):
            for c in range(C):
                dis.append((abs(r0 - r) + abs(c0 - c), [r, c]))
        dis.sort()
        return [x for d, x in dis]


t = Solution()
print(t.allCellsDistOrder(2, 2, 0, 1))
