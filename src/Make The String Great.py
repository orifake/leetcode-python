class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for char in s[1:]:
            if stack and char.lower() == stack[-1].lower(
            ) and char != stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


t = Solution()
print(t.makeGood("leEeetcode"))