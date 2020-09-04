from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        i = 0

        while i + 1 < N and A[i] < A[i + 1]:
            i += 1
        if i == 0 or i == N - 1:
            return False

        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1


t = Solution()
print(t.validMountainArray([0, 3, 2, 1]))
print(t.validMountainArray([2, 1]))
print(t.validMountainArray([3, 5, 5]))
