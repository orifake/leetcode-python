from typing import List


class Solution:
    def createTargetArray(self, nums: List[int],
                          index: List[int]) -> List[int]:
        ans = []
        for i in range(len(index)):
            ans.insert(index[i], nums[i])  # insert(位置, 值)
        return ans


t = Solution()
print(t.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
