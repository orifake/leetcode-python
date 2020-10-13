class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if n & 1 else "a" * (n - 1) + "b"


t = Solution()
print(t.generateTheString(4))