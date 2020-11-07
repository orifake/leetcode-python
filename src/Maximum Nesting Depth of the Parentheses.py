class Solution:
    def maxDepth(self, s: str) -> int:
        ans = curr = 0
        for char in s:
            if char == '(':
                curr += 1
                ans = max(ans, curr)
            elif char == ')':
                curr -= 1
        return ans


t = Solution()
print(t.maxDepth("(1)+((2))+(((3)))"))