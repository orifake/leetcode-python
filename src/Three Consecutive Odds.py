from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        stack = []
        for i in arr:
            if i % 2 == 0:
                stack = []
            elif len(stack) == 2:
                return True
            else:
                stack.append(i)
        return False


t = Solution()
print(t.threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
