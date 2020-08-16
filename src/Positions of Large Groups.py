from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    ans.append([i, j])
                i = j + 1
        return ans


t = Solution()
print(t.largeGroupPositions("abcdddeeeeaabbbcd"))