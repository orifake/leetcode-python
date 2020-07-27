from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        dict1 = {}

        for i in range(len(nums)):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1
            if dict1.get(nums[i] + 1):
                ans = max(ans, dict1.get(nums[i]) + dict1.get(nums[i] + 1))
            if dict1.get(nums[i] - 1):
                ans = max(ans, dict1.get(nums[i]) + dict1.get(nums[i] - 1))
        return ans


t = Solution()
print(t.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
