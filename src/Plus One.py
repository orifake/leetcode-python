from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        add = 1
        i = len(digits) - 1
        while i >= 0:
            sum = digits[i] + add
            i = i - 1
            if sum == 10:
                add = 1
                sum = 0
            else:
                add = 0
            result.insert(0, sum)
        if add == 1:
            result.insert(0, 1)

        return result


t = Solution()
print(t.plusOne([9, 9, 9]))
