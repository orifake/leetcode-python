from typing import List
import collections


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int,
                      c: int) -> List[List[int]]:
        d = collections.deque(sum(nums, []))
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            return [[d.popleft() for i in range(c)] for j in range(r)]