from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + int((Sb - Sa) / 2)]


t = Solution()
print(t.fairCandySwap([1, 2, 5], [2, 4]))
