class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        result = []
        for i in reversed(range(len(S))):
            if S[i] == '-':
                continue
            if len(result) % (K + 1) == K:
                result += '-'
            result += S[i].upper()
        return "".join(reversed(result))


t = Solution()
print(t.licenseKeyFormatting("2-5g-3-J", 2))
print(t.licenseKeyFormatting("5F3Z-2e-9-w", 4))
