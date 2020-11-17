from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        lookup = {x[0]: i for i, x in enumerate(pieces)}
        i = 0

        while i < len(arr):
            if arr[i] not in lookup:
                return False
            for c in pieces[lookup[arr[i]]]:
                if i == len(arr) or arr[i] != c:
                    return False
                i += 1
        return True


t = Solution()
print(t.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
