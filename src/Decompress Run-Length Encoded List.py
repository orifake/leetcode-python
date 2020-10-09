from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            ans.extend(nums[i]*[nums[i+1]])
        return ans


t = Solution()
print(t.decompressRLElist([1, 1, 2, 3]))
