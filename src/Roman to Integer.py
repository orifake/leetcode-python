class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I': 1,
            'X': 10,
            'C': 100,
            'M': 1000,
            'V': 5,
            'L': 50,
            'D': 500
        }
        sum = 0
        i = 0
        length = len(s)
        while (i < length):
            roman = hash[s[i]]
            nextRoman = 0
            if i + 1 == length:
                nextRoman = 0
            else:
                nextRoman = hash[s[i + 1]]
            if nextRoman > roman:
                sum += (nextRoman - roman)
                i += 1
            else:
                sum += roman
            i += 1
        return sum


t = Solution()
# print(t.romanToInt('LVIII'))
print(t.romanToInt('IV'))