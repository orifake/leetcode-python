from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                if i == len(bits):
                    return False
            else:
                i += 1
        return True


t = Solution()
print(t.isOneBitCharacter([1, 0, 0]))
