from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ans = 0
        rows = [0] * n
        cols = [0] * m

        for i, j in indices:
            rows[i] = rows[i] ^ 1
            cols[j] = cols[j] ^ 1

        for i in range(n):
            for j in range(m):
                if (rows[i] ^ cols[j] == 1):
                    ans += 1

        return ans


t = Solution()
print(t.oddCells(2, 3, [[0, 1], [1, 1]]))
