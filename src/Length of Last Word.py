class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or not s.split():
            return 0
        return len(s.split()[-1])