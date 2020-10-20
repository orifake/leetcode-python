from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1 = max_2 = 0

        for num in nums:
            if num > max_1:
                max_1, max_2 = num, max_1
            elif num > max_2:
                max_2 = num
        return (max_1 - 1) * (max_2 - 1)


t = Solution()
print(t.maxProduct([3, 4, 5, 2]))
