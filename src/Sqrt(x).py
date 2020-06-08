class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x

        if x == 0:
            return 0

        while low + 1 < high:
            mid = low + int((high - low) / 2)
            if mid * mid <= x:
                low = mid
            else:
                high = mid

        return low


t = Solution()
print(t.mySqrt(8))