from typing import List
import sys


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = -sys.maxsize
        ans = []

        for i, s in enumerate(S):
            if s == C:
                prev = i
            ans.append(i - prev)

        prev = sys.maxsize
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans


t = Solution()
print(t.shortestToChar("loveleetcode", "e"))
