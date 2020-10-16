from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_num = sorted(nums)
        sum_subsequence = 0
        sum_nums = sum(nums)
        for i in range(len(nums)):
            item = sorted_num[len(nums) - i - 1]
            sum_subsequence += item
            sum_nums -= item
            ans.append(item)
            if sum_subsequence > sum_nums:
                return ans
        return ans


t = Solution()
print(t.minSubsequence([4, 3, 10, 9, 8]))
