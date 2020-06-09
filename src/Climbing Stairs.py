class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1] * (n + 1)
        for i in range(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]


t = Solution()
print(t.climbStairs(3))