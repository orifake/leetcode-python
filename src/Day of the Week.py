class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_list = [
            "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday",
            "Wednesday"
        ]
        count = 0
        for i in range(1971, year):
            count += 366 if self.isLeapYear(i) else 365

        count += self.dayOfYear(day, month, year)
        return day_list[count % 7]

    def isLeapYear(self, year):
        return (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0

    def dayOfYear(self, day: int, month: int, year: int) -> int:
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear(year):
            month_list[1] += 1

        return sum(month_list[:month - 1]) + day


t = Solution()
print(t.dayOfTheWeek(18, 7, 1999))
