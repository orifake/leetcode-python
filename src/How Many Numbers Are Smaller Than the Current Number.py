from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        for num in nums:
            ans.append(sorted_nums.index(num))

        return ans


t = Solution()
print(t.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
