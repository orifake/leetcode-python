class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 1 if x >= 0 else -1
        result = 0
        temp = 0
        x = abs(x)
        while x:
            temp = x % 10
            result = temp + result * 10

            x = int(x / 10)

        return (result * flag) if result < 2147483648 and result >= -2147483648 else 0


t = Solution()
print(t.reverse(-321))