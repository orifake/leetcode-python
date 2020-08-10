class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(map(S.count, J))


t = Solution()
print(t.numJewelsInStones("aA", "aAAbbbb"))
