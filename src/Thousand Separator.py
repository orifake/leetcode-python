class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")


t = Solution()
print(t.thousandSeparator(1234))