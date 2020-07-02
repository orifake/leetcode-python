class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        loop = [2, 3, 5]

        for i in loop:
            while num % i == 0:
                num = num / i

        return num == 1