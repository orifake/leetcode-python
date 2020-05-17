from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in h:
                h[num] = i
            else:
                return [h[complement], i]

t = Solution()
print(t.twoSum([2, 7, 11, 15],9))