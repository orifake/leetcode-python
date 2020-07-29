from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        ans = sum
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            ans = max(ans, sum)

        return ans / k


t = Solution()
print(t.findMaxAverage([0, 1, 1, 3, 3], 4))
