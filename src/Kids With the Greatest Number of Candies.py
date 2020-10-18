from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int],
                        extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for num in candies:
            if num + extraCandies >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans


t = Solution()
print(t.kidsWithCandies([2, 3, 5, 1, 3], 3))
