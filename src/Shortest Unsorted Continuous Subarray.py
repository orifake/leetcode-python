from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums == nums:
            return 0
        length = len(nums)
        left = 0
        right = length - 1
        while left < length and nums[left] == sorted_nums[left]:
            left += 1
        while right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1

        return right - left + 1

t = Solution()
print(t.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
