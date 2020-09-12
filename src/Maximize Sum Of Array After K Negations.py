from typing import List
import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A_sum = sum(A)
        heapq.heapify(A)

        while K > 0:
            A_min = heapq.heappop(A)
            heapq.heappush(A, -A_min)
            K -= 1
            A_sum += (-2 * A_min)

        return A_sum


t = Solution()
print(t.largestSumAfterKNegations([3, -1, 0, 2], 3))
