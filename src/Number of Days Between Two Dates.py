class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self.countDays(date1) - self.countDays(date2))

    def countDays(self, date: str) -> int:
        count = 0
        [year, month, day] = map(int, date.split('-'))
        for i in range(1971, year):
            count += 366 if self.isLeapYear(i) else 365

        count += self.dayOfYear(day, month, year)
        return count

    def isLeapYear(self, year):
        return (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0

    def dayOfYear(self, day: int, month: int, year: int) -> int:
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear(year):
            month_list[1] += 1

        return sum(month_list[:month - 1]) + day


t = Solution()
print(t.daysBetweenDates("2019-06-29", "2019-06-30"))
