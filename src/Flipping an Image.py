from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range(int((len(row) + 1) / 2)):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1

        return A

t = Solution()
print(t.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))