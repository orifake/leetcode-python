class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, left = 0, 0
        lookup = {}
        for right in range(len(s)):
            if s[right] in lookup:
                left = max(left, lookup[s[right]] + 1)
            lookup[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans


t = Solution()
print(t.lengthOfLongestSubstring("abcabcbb"))