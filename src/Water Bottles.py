class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        full = numBottles
        empty = 0
        while full:
            ans += full
            empty += full
            # exchange
            full = int(empty / numExchange)
            empty = empty % numExchange
        return ans


t = Solution()
print(t.numWaterBottles(9, 3))
