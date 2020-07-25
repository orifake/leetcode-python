from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        kinds = len(set(candies))
        nums = int(len(candies) / 2)

        if kinds < nums:
            return kinds
        else:
            return nums
