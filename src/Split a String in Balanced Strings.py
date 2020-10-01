class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced = 0
        ans = 0
        for char in s:
            if char == 'L':
                balanced += 1
            else:
                balanced -= 1

            if balanced == 0:
                ans += 1
        return ans


t = Solution()
print(t.balancedStringSplit("RLLLLRRRLR"))