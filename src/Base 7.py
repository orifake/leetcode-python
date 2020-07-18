class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        new_num = abs(num)
        ans = ""
        while new_num:
            ans = str(new_num % 7) + ans
            new_num //= 7

        return ans if num > 0 else "-" + ans


t = Solution()
print(t.convertToBase7(100))
print(t.convertToBase7(-7))