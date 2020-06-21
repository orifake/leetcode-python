from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        for i in range(0, k):
            temp = nums.pop()
            nums.insert(0, temp)

        return nums


t = Solution()
print(t.rotate([1, 2, 3, 4, 5, 6, 7], 3))
