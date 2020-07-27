from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {j: i for i, j in enumerate(list1)}
        ans = []
        minsum = len(list1) + len(list2)
        for x, y in enumerate(list2):
            if y not in dict1:
                continue
            currentsum = x + dict1[y]
            if currentsum < minsum:
                ans = [y]
                minsum = currentsum
            elif currentsum == minsum:
                ans.append(y)
        return ans