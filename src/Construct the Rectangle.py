from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        height = int(area**0.5)
        width = int(area / height)
        while area % height != 0 or width > height:
            height += 1

        return [height, int(area / height)]


t = Solution()
print(t.constructRectangle(5))