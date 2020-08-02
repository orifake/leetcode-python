from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 1
        anchor = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                anchor = i
            ans = max(ans, i - anchor + 1)

        return ans


t = Solution()
print(t.findLengthOfLCIS([7, 8, 9, 1, 4, 3]))
