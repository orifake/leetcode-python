from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1

        return ans

t = Solution()
print(t.findNumbers([555,901,482,1771]))