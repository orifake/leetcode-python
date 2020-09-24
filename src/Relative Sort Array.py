from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        in_arr1 = []
        not_in_arr1 = []
        for i in arr1:
            if i in arr2:
                in_arr1.append(i)
            else:
                not_in_arr1.append(i)
        temp = sorted(in_arr1, key=list(arr2).index)
        result = temp + sorted(not_in_arr1)
        return result


t = Solution()
print(
    t.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
                        [2, 1, 4, 3, 9, 6]))