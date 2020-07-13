from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        numset = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in numset:
                ans.append(num)
        return ans