class Solution:
    def countSegments(self, s):
        result = int(len(s) and s[-1] != ' ')
        for i in range(1, len(s)):
            if s[i] == ' ' and s[i - 1] != ' ':
                result += 1
        return result


t = Solution()
print(t.countSegments("Hello, my name is John"))