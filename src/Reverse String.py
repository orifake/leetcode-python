from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]


t = Solution()
print(t.reverseString(["h", "e", "l", "l", "o"]))

t2 = Solution2()
print(t2.reverseString(["h", "e", "l", "l", "o"]))