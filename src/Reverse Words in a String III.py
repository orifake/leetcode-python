class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''

        list = s.split(' ')
        ans = []
        for word in list:
            ans.append(word[::-1])

        return ' '.join(ans)

t = Solution()
print(t.reverseWords("Let's take LeetCode contest"))