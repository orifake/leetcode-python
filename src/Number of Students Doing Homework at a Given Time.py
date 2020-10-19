from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int],
                    queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))


t = Solution()
print(t.busyStudent([1, 2, 3], [3, 2, 7], 4))
