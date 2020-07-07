class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for word in magazine:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1
        for word in ransomNote:
            if word not in m or m[word] < 1:
                return False
            else:
                m[word] -= 1
        return True


t = Solution()
print(t.canConstruct("aa", "aab"))
