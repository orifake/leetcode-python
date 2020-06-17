from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result


t = Solution()
print(t.singleNumber([4, 1, 2, 1, 2]))
