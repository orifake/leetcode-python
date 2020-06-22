from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0

        if length == 1:
            return nums[0]
        result = []
        result.append(nums[0])
        result.append(max(nums[0], nums[1]))

        for i in range(2, length):
            result.append(max((result[i - 2] + nums[i], result[i - 1])))
        return result[-1]

t = Solution()
print(t.rob([2,7,9,3,1]))