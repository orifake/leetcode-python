class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
        for i in range(len(t)):
            if t[i] in dict1 and dict1[t[i]] > 0:
                dict1[t[i]] -= 1
            else:
                return t[i]


t = Solution()
print(t.findTheDifference("abcd", "abcde"))
print(t.findTheDifference("a", "aa"))
