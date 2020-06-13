from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[]] * numRows
        for i in range(0, numRows):
            result[i] = [1] * (i + 1)
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result


t = Solution()
print(t.generate(5))