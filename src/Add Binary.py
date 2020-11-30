class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     return bin(int(a, 2) + int(b, 2))[2:]
    def addBinary(self, a: str, b: str) -> str:
        ans, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = divmod(val, 2)
            ans += str(val)
        if carry:
            ans += str(carry)
        return ans[::-1]


t = Solution()
print(t.addBinary('1', '11'))
