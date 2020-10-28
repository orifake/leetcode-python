class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - ((low - 1) + 1) // 2


t = Solution()
print(t.countOdds(3, 7))
