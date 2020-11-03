from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = [0] * len(mat), [0] * len(mat[0])
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        result = 0
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j] == rows[i] == cols[j] == 1:
                    result += 1
        return result


t = Solution()
print(t.numSpecial([[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]))
