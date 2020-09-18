from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
                if x != y:
                    heapq.heappush(stones, -abs(x - y))
        return 0 if not stones else -stones[0]


t = Solution()
print(t.lastStoneWeight([2, 7, 4, 1, 8, 1]))
