class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = ''
        while i < len(s):
            if i < len(s) - 2:
                if s[i+2] == '#':
                    ans += chr(96 + int(s[i:i + 2]))
                    s = s[:i] + '' + s[i + 3:]
                else:
                    ans += chr(96 + int(s[i]))
                    s = s[:i] + '' + s[i + 1:]
            else:
                ans += chr(96 + int(s[i]))
                i += 1
        return ans


t = Solution()
print(t.freqAlphabets("10#11#12"))
