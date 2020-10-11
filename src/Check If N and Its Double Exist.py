from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_set = set()
        for num in arr:
            if 2*num in num_set or (num % 2 == 0 and int(num/2) in num_set):
                return True
            num_set.add(num)

        return False


t = Solution()
print(t.checkIfExist([10, 2, 5, 3]))
