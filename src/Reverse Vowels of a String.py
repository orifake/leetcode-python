class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        pos = []
        result = list(s)
        for i, s in enumerate(s):
            if s in vowels:
                pos.append((i, s))

        for j in range(int(len(pos) / 2)):
            result[pos[j][0]] = pos[len(pos) - j - 1][1]
            result[pos[len(pos) - j - 1][0]] = pos[j][1]

        return "".join(result)


t = Solution()
print(t.reverseVowels("leetcode"))