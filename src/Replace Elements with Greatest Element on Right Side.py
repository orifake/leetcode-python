from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        if len(arr) == 1:
            return ans
        max_right = -1
        length = len(arr)
        for i in range(0, length-1):
            max_right = max(max_right, arr[length-1-i])
            ans.insert(0, max_right)

        return ans


t = Solution()
print(t.replaceElements([17, 18, 5, 4, 6, 1]))
