from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        prefix = 0
        for a in A:
            prefix = (prefix * 2 + a) % 5
            ans.append(prefix == 0)

        return ans


t = Solution()
print(t.prefixesDivBy5([0, 1, 1, 1, 1, 1]))
