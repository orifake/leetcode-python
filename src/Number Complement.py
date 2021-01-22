class Solution:
    def findComplement(self, num):
        i = 1
        while i <= num:
            i *= 2
        if i == num:
            return i - 1
        else:
            return i - 1 - num


t = Solution()
print(t.findComplement(5))
