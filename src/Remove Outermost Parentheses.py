class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = ''
        prev_i = 0
        count = 0
        for i, s in enumerate(S):
            if s == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                ans += S[prev_i + 1:i]
                prev_i = i + 1
        return ans


t = Solution()
print(t.removeOuterParentheses("(()())(())(()(()))"))