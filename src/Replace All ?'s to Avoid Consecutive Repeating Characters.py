class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] != '?':
                continue
            else:
                for c in ('a', 'b', 'c'):
                    if (i == 0 or s[i - 1] != c) and (i == len(s) - 1
                                                      or c != s[i + 1]):
                        break
            s[i] = c
        return "".join(s)


t = Solution()
print(t.modifyString("j?qg??b"))