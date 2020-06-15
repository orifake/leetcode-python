class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = -1
        j = len(s)
        while True:
            i += 1
            j -= 1
            if i > j:
                return True
            while i < j:
                if not s[i].isalnum():
                    i += 1
                else:
                    break

            while i < j:
                if not s[j].isalnum():
                    j -= 1
                else:
                    break

            if s[i].lower() != s[j].lower():
                return False

t = Solution()
print(t.isPalindrome("A man, a plan, a canal: Panama"))
print(t.isPalindrome("race a car"))