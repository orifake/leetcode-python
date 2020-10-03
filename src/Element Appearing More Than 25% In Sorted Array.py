from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 1
        length = len(arr) / 4

        for i in range(0, len(arr) - 1):
            if arr[i] == arr[i + 1]:
                count += 1
                if count > length:
                    return arr[i]
            else:
                count = 1

        return arr[0]


t = Solution()
print(t.findSpecialInteger([1, 2, 3, 3]))
