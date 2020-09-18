from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        graph = [[] for i in range(N)]
        for path in paths:
            graph[path[0] - 1].append(path[1] - 1)
            graph[path[1] - 1].append(path[0] - 1)
        for i in range(N):
            neighbor_colors = []
            for neighbor in graph[i]:
                neighbor_colors.append(res[neighbor])
            for color in range(1, 5):
                if color in neighbor_colors:
                    continue
                res[i] = color
                break
        return res


t = Solution()
print(t.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]))
