class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     return bin(int(a, 2) + int(b, 2))[2:]
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        i, j, plus = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or plus == 1:
            plus += int(a[i]) if i >= 0 else 0
            plus += int(b[j]) if j >= 0 else 0
            result = str(plus % 2) + result
            i, j, plus = i - 1, j - 1, int(plus / 2)

        return result


t = Solution()
print(t.addBinary('1', '11'))
