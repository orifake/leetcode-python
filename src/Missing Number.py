from typing import List
from functools import reduce
import operator


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums, \
                      reduce(operator.xor, range(len(nums) + 1)))


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


t = Solution()
print(t.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
