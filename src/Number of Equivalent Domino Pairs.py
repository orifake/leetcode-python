from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = {}
        ans = 0
        for (i, j) in dominoes:
            if (i, j) in dic:
                ans += dic[(i, j)]
            if i != j and (j, i) in dic:
                ans += dic[(j, i)]
            dic[(i, j)] = dic.setdefault((i, j), 0) + 1
        return ans


t = Solution()
print(t.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
