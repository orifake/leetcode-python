class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1] * (n + 1)
        for i in range(2, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]


# Time:  O(n)
# Space: O(1)
class Solution2:
    def climbStairs(self, n: int) -> int:
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current,
        return current


t = Solution()
print(t.climbStairs(3))