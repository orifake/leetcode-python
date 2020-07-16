from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            radius = 0x7FFFFFFF
            le = bisect.bisect_right(heaters, house)
            if le > 0:
                radius = min(radius, house - heaters[le - 1])
            ge = bisect.bisect_left(heaters, house)
            if ge < len(heaters):
                radius = min(radius, heaters[ge] - house)
            ans = max(ans, radius)
        return ans