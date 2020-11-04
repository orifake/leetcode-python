from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        cnt = 0
        for i in range(len(arr) - m):
            if arr[i] != arr[i + m]:
                cnt = 0
                continue
            cnt += 1
            if cnt == (k - 1) * m:
                return True
        return False


t = Solution()
print(t.containsPattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2))
