class Solution:
    def maxPower(self, s: str) -> int:
        count, max_count, prev = 0, 0, None
        for char in s:
            if char == prev:
                count += 1
            else:
                prev = char
                count = 1
            max_count = max(max_count, count)

        return max_count


t = Solution()
print(t.maxPower("abbcccddddeeeeedcba"))