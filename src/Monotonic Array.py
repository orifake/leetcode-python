from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                increasing = False
            if A[i] < A[i + 1]:
                decreasing = False

        return increasing or decreasing


t = Solution()
print(t.isMonotonic([1, 3, 2]))
