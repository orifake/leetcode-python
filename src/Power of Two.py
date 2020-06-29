class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


t = Solution()
print(t.isPowerOfTwo(16))
print(t.isPowerOfTwo(218))