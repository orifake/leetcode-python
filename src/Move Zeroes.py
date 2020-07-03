from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            index = len(nums) - 1 - i
            if nums[index] == 0:
                nums.append(0)
                nums.pop(index)


t = Solution()
print(t.moveZeroes([0, 0, 1]))
