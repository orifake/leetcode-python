from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        ans = []
        for i in nums:
            running_sum += i
            ans.append(running_sum)

        return ans


t = Solution()
print(t.runningSum([3, 1, 2, 10, 1]))
