class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        Mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) & Mask
            a = (a ^ b) & Mask
            b = carry << 1

        return a if a <= MAX else ~(a ^ Mask)


t = Solution()
print(t.getSum(-12, -8))
