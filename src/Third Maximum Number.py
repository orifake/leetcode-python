from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        queue = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if num in queue:
                continue

            if num > queue[0] or len(queue) <= 3:
                queue.append(num)
                queue.sort()
                if len(queue) > 3:
                    queue.pop(0)

        if len(queue) == 3:
            return queue[0]
        else:
            return queue[-1]


t = Solution()
print(t.thirdMax([2, 2, 3, 1]))
