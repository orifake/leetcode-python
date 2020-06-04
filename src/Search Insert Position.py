class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return low