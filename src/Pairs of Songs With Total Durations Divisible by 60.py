from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        records = {}
        ans = 0

        for i in time:
            ans += records.get((60 - i % 60) % 60, 0)
            if i % 60 in records:
                records[i % 60] += 1
            else:
                records[i % 60] = 1

        return ans


t = Solution()
print(t.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
