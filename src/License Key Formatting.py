class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.upper().replace('-', '')
        first = len(s) % K
        ans = []
        if first > 0:
            ans.append(s[:first])
        i = first
        while i < len(s):
            ans.append(s[i:i + K])
            i += K
        return '-'.join(ans)


t = Solution()
print(t.licenseKeyFormatting("2-5g-3-J", 2))
print(t.licenseKeyFormatting("5F3Z-2e-9-w", 4))
