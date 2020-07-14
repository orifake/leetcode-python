from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            a = {}
            for j in points:
                c = (i[0] - j[0])**2 + (i[1] - j[1])**2
                if c not in a:
                    a[c] = 1
                else:
                    ans += a[c]
                    a[c] += 1
        return ans * 2


t = Solution()
print(t.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
