from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        for i in range(2,len(coordinates)):
            if not self.isLine(coordinates[0],coordinates[1],coordinates[i]):
                return False

        return True


    def isLine(self, p0, p1, p2):
        a = p1[1] - p0[1]
        b = p1[0] - p0[0]
        c = p2[1] - p0[1]
        d = p2[0] - p0[0]

        return True if (a * d == b * c) else False

t = Solution()
print(t.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))