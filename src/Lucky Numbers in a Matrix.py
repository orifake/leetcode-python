from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_r = {min(rows) for rows in matrix}
        max_c = {max(columns) for columns in zip(*matrix)}
        return list(min_r & max_c)


t = Solution()
print(t.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
