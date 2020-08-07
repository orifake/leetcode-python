class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for s in str:
            if ord(s) >= ord('A') and ord(s) <= ord('Z'):
                ans += chr(ord(s) - ord('A') + ord('a'))
            else:
                ans += s
        return ans


t = Solution()
print(t.toLowerCase("Hello"))