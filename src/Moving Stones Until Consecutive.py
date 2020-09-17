from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones_list = [a, b, c]
        stones_list.sort()
        a, b, c = stones_list
        if b - a == 1 and c - b == 1:
            return [0, 0]
        min_moves = 2

        if b - a == 1 or c - b == 1 or c - b == 2 or b - a == 2:
            min_moves -= 1

        max_moves = c - a
        max_moves -= 2
        return [min_moves, max_moves]


t = Solution()
print(t.numMovesStones(3, 5, 1))
