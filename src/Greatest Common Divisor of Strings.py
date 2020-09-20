class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):  # Time: O((logn)^2)
            while b:
                a, b = b, a % b
            return a

        def check(s, common):
            i = 0
            for c in s:
                if c != common[i]:
                    return False
                i = (i + 1) % len(common)
            return True

        if not str1 or not str2:
            return ""

        c = gcd(len(str1), len(str2))
        result = str1[:c]
        return result if check(str1, result) and check(str2, result) else ""


t = Solution()
print(t.gcdOfStrings("ABABAB", "ABAB"))
