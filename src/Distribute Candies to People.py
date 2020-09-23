from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        num = 0
        while candies > 0:
            ans[num % num_people] += min(num + 1, candies)
            num += 1
            candies -= num

        return ans


t = Solution()
print(t.distributeCandies(10, 3))
