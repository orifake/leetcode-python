from typing import List

# Time:  O(n)
# Space: O(n)


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


# Time:  O(n)
# Space: O(1)
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits


t = Solution()
print(t.plusOne([9, 9, 9]))
