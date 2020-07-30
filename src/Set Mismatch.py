from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = -1
        missing = 1
        length = len(nums)
        for i in range(1, length):
            if (nums[i] == nums[i - 1]):
                dup = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1

        if nums[length - 1] != length:
            return [dup, length]
        else:
            return [dup, missing]


t = Solution()
print(t.findErrorNums([1, 2, 2, 4]))
