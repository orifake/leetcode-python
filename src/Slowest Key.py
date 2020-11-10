from typing import List
import collections


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result, lookup = 'a', collections.Counter()
        for i, c in enumerate(keysPressed):
            lookup[c] = max(
                lookup[c],
                releaseTimes[i] - (releaseTimes[i - 1] if i > 0 else 0))
            if lookup[c] > lookup[result] or lookup[c] == lookup[
                    result] and c > result:
                result = c
        return result


t = Solution()
print(t.slowestKey([12, 23, 36, 46, 62], "spuda"))
