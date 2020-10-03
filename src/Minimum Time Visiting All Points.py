from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            dis_x = abs(points[i][0] - points[i + 1][0])
            dis_y = abs(points[i][1] - points[i + 1][1])
            ans += min(dis_x, dis_y)
            ans += max(dis_x, dis_y) - min(dis_x, dis_y)

        return ans


t = Solution()
print(t.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
