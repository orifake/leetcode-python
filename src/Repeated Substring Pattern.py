class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i == 0:
                sub = s[:i]
                repeat = length // i
                if sub * repeat == s:
                    return True
        return False

t = Solution()
print(t.repeatedSubstringPattern("abab"))