from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                # If the value occurs before, check the difference.
                if i - lookup[num] <= k:
                    return True
                # Update the index of the value.
                lookup[num] = i
        return False


t = Solution()
print(t.containsNearbyDuplicate([1, 0, 1, 1], 1))
