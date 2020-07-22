class Solution:
    def checkRecord(self, s: str) -> bool:
        a = s.count('A')
        l = s.count('LLL')
        if a > 1 or l > 0:
            return False
        return True