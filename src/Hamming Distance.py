class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        while z:
            ans += z % 2
            z = int(z / 2)
        return ans