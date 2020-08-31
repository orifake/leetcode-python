class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)

        return "".join(ans)

t = Solution()
print(t.reverseOnlyLetters("Test1ng-Leet=code-Q!"))