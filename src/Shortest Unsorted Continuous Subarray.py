from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -2
        min_from_right, max_from_left = nums[-1], nums[0]
        for i in range(1, n):
            max_from_left = max(max_from_left, nums[i])
            min_from_right = min(min_from_right, nums[n - 1 - i])
            if nums[i] < max_from_left: right = i
            if nums[n - 1 - i] > min_from_right: left = n - 1 - i
        return right - left + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
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
