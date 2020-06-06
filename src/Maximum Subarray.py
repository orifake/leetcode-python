from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length     
        dp[0] = nums[0]
        maxsum = dp[0]
        
        for i in range(1, length):
            if dp[i - 1] + nums[i] >= nums[i]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            if dp[i] >= maxsum:
                maxsum = dp[i]
            
                    
        return maxsum 

t = Solution()
print(t.maxSubArray([-2, -1]))
