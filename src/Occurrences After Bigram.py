from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        ans = []
        for i in range(len(words) - 2):
            f, s, t = words[i], words[i + 1], words[i + 2]
            if f == first and s == second:
                ans.append(t)
        return ans


t = Solution()
print(t.findOcurrences("we will we will rock you", "we", "will"))
