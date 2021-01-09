import math

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (num & (num - 1)) == 0 and \
               ((num & 0b01010101010101010101010101010101) == num)

class Solution2:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return (math.log10(num) / math.log10(4)) % 1 == 0


t = Solution()
print(t.isPowerOfFour(4))