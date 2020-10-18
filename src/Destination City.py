from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()


t = Solution()
print(
    t.destCity([["London", "New York"], ["New York", "Lima"],
                ["Lima", "Sao Paulo"]]))
