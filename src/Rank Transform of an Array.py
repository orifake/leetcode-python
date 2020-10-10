from typing import List
import bisect


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))
        ans = []
        for i in arr:
            inx = bisect.bisect_left(sorted_arr, i)
            ans.append(inx + 1)
        return ans


t = Solution()
print(t.arrayRankTransform([40, 10, 20, 30]))
