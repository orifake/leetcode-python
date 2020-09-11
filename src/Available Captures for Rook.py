from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        N = 8
        x, y = -1, -1
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break

        for i in range(x + 1, N):
            if board[i][y] == 'B':
                break
            elif board[i][y] == 'p':
                ans += 1
                break

        for i in range(x - 1, -1, -1):
            if board[i][y] == 'B':
                break
            elif board[i][y] == 'p':
                ans += 1
                break

        for j in range(y + 1, N):
            if board[x][j] == 'B':
                break
            elif board[x][j] == 'p':
                ans += 1
                break

        for j in range(y - 1, -1, -1):
            if board[x][j] == 'B':
                break
            elif board[x][j] == 'p':
                ans += 1
                break

        return ans


t = Solution()
print(
    t.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."],
                       [".", "p", "p", "p", "p", "p", ".", "."],
                       [".", "p", "p", "B", "p", "p", ".", "."],
                       [".", "p", "B", "R", "B", "p", ".", "."],
                       [".", "p", "p", "B", "p", "p", ".", "."],
                       [".", "p", "p", "p", "p", "p", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", ".", ".", "."]]))
