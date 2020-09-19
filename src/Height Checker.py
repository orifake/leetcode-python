from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if sort[i] != heights[i]:
                count += 1
        return count


t = Solution()
print(t.heightChecker([1, 1, 4, 2, 1, 3]))
