from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        B = set(A[0])
        ans = []
        for i in B:
            n = min([a_word.count(i) for a_word in A])
            if n:
                ans.extend([i]*n)
        return ans


t = Solution()
print(t.commonChars(["cool", "lock", "cook"]))
