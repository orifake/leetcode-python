class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num

        while low <= high:
            mid = int((low + high) / 2)
            if mid * mid < num:
                low = mid + 1
            elif mid * mid > num:
                high = mid - 1
            else:
                return True
        return False

t = Solution()
print(t.isPerfectSquare(14))