from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def check(arr, k, x):
            return arr[x] - (x + 1) < k

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if not check(arr, k, mid):
                right = mid - 1
            else:
                left = mid + 1
        return right + 1 + k


t = Solution()
print(t.findKthPositive([2, 3, 4, 7, 11], 5))
