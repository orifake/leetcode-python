from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        s = [(self.hammingWeight(num), num) for num in arr]
        r = sorted(s)
        return [r[1] for r in r]

    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += 1
            n &= (n - 1)

        return sum


t = Solution()
print(t.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
print(t.sortByBits([10000, 10000]))
