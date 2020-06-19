class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ''
        while n:
            result = chr((int(n) - 1) % 26 + 65) + result
            n = int((int(n) - 1) / 26)
        return result

t = Solution()
print(t.convertToTitle('2'))