class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(0, 32):
            result <<= 1
            result |= ((n >> i) & 1)
        return result