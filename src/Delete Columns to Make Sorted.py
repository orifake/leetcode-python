from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i + 1] for i in range(len(col) - 1)):
                ans += 1
        return ans


t = Solution()
print(t.minDeletionSize(["zyx", "wvu", "tsr"]))
