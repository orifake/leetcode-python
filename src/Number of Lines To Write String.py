from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line = 1
        width = 0
        for letter in S:
            w = widths[ord(letter) - ord('a')]
            line = line + 1 if w + width > 100 else line
            width = w if w + width > 100 else w + width

        return line, width


t = Solution()
print(
    t.numberOfLines([
        10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10
    ], "abcdefghijklmnopqrstuvwxyz"))
