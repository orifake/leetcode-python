class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictS = dict()
        dictT = dict()
        for i in range(0, len(s)):
            curS = s[i]
            curT = t[i]
            if dictS.get(curS) is None:
                dictS[curS] = curT
            elif dictS.get(curS) != curT:
                return False

            if dictT.get(curT) is None:
                dictT[curT] = curS
            elif dictT.get(curT) != curS:
                return False
        return True


t = Solution()
print(t.isIsomorphic("ab", "ba"))
