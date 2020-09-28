from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int,
                                destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        sum_clockwise = sum(distance[start:destination])

        return min(sum_clockwise, sum(distance) - sum_clockwise)


t = Solution()
print(t.distanceBetweenBusStops([1, 2, 3, 4], 0, 2))
