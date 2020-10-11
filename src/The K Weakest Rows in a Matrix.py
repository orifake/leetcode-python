from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s = [(sum(m), i) for i, m in enumerate(mat)]
        r = sorted(s)
        return [r[1] for r in r[:k]]


t = Solution()
print(t.kWeakestRows([[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]], 3))
