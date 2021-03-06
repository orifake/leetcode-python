from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return -1


t = Solution()
print(t.search([-1, 0, 3, 5, 9, 12], 2))
print(t.search([-1,0,3,5,9,12], 9))
