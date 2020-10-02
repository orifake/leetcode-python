from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(k):
            previous = grid[-1][-1]
            for row in range(rows):
                for col in range(cols):
                    temp = grid[row][col]
                    grid[row][col] = previous
                    previous = temp
        return grid


t = Solution()
print(
    t.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
                4))
