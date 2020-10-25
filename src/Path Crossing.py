from typing import List


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        path_set = set()
        cur = (0, 0)
        path_set.add(cur)
        for p in path:
            if p == 'N':
                cur = (cur[0], cur[1] + 1)
            elif p == 'S':
                cur = (cur[0], cur[1] - 1)
            elif p == 'E':
                cur = (cur[0] + 1, cur[1])
            else:
                cur = (cur[0] - 1, cur[1])

            if cur in path_set:
                return True
            else:
                path_set.add(cur)

        return False


t = Solution()
print(t.isPathCrossing("NESWW"))