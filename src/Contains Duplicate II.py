from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        queue = set([])
        for i in range(0, len(nums)):
            if i > k:
                queue.remove(nums[i - k - 1])
            if nums[i] in queue:
                return True
            else:
                queue.add(nums[i])
        return False


t = Solution()
print(t.containsNearbyDuplicate([1, 0, 1, 1], 1))
