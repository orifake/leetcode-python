class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in h:
                h[num] = i
            else:
                return [h[complement], i]