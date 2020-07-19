from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sorted_nums = nums.copy()
        sorted_nums.sort(reverse=True)
        m = {}
        l = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = []
        for i, num in enumerate(sorted_nums):
            if i < len(l):
                m[num] = l[i]
            else:
                m[num] = str(i + 1)

        for num in nums:
            ans.append(m[num])
        return ans


t = Solution()
print(t.findRelativeRanks([10, 3, 8, 9, 4]))
