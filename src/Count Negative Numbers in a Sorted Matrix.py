from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        r = rows - 1
        c = 0
        while r >= 0 and c < cols:
            if grid[r][c] < 0:
                r -= 1
                count += cols - c
            else:
                c += 1
        return count


t = Solution()
print(
    t.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2],
                      [-1, -1, -2, -3]]))
