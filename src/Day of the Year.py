class Solution:
    def dayOfYear(self, date: str) -> int:
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        [year, month, day] = map(int, date.split('-'))

        def isLeapYear(year):
            return (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0

        if isLeapYear(year):
            month_list[1] += 1

        return sum(month_list[:month - 1]) + day


t = Solution()
print(t.dayOfYear("2019-02-10"))