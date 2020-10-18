from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        curr = 1

        for t in target:
            ans.extend(["Push", "Pop"] * (t - curr))
            ans.append("Push")
            curr = t + 1

        return ans


t = Solution()
print(t.buildArray([1, 3], 3))
