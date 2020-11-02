from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]
        # if start < end, all the numbers between [start,end] inclusive will appear for the most times
        if start <= end:
            return list(range(start, end + 1))
        # else, the numbers between (end,start) exlusive will appear for 1 less times
        else:
            exclude = list(range(end + 1, start))
            return [i for i in range(1, n + 1) if i not in exclude]


t = Solution()
print(t.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]))
