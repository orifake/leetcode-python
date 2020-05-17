import re


class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        total = 0
        while temp > 0:
            total = total * 10 + temp % 10
            temp //= 10
        return x == total


t = Solution()
print(t.isPalindrome(121))
