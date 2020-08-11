from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [
                    path + letter for path in res
                    for letter in [ch.lower(), ch.upper()]
                ]
            else:
                res = [path + ch for path in res]

        return res


t = Solution()
print(t.letterCasePermutation("a1b2"))
