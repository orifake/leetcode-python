from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            if self.selfDividing(num):
                ans.append(num)
        return ans

    def selfDividing(self, n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                return False
        return True


t = Solution()
print(t.selfDividingNumbers(1, 22))
