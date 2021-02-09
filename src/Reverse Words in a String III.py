class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = [word[::-1] for word in s.split(' ')]
        return ' '.join(reversed_words)


t = Solution()
print(t.reverseWords("Let's take LeetCode contest"))