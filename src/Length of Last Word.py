# Time:  O(n)
# Space: O(n)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or not s.split():
            return 0
        return len(s.split()[-1])


# Time:  O(n)
# Space: O(1)
class Solution2:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length