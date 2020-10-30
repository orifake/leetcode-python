from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for i, c in zip(indices, s):
            result[i] = c
        return "".join(result)


t = Solution()
print(t.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
