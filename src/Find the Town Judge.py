from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N <= 0:
            return -1

        if not len(trust) and N == 1:
            return 1

        ans = -1
        trust_map = {}
        judge_set = set()

        for i in range(0, len(trust)):
            [a, b] = trust[i]
            if b in trust_map:
                trust_map[b] += 1
            else:
                trust_map[b] = 1
            judge_set.add(a)

        for p in trust_map:
            if trust_map[p] == N - 1 and p not in judge_set:
                ans = p

        return ans


t = Solution()
print(t.findJudge(1,[]))
print(t.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(t.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
