from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i

            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for num in nums:
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)
        return ans


t = Solution()
print(t.findShortestSubArray([1, 2, 2, 3, 1]))
