class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i, string in enumerate(s):
            index = t.find(string)
            if index > -1:
                t = t[0:index] + t[index + 1:]
            else:
                return False

        return True


t = Solution()
print(t.isAnagram('anagram', 'nagaram'))
print(t.isAnagram('rat', 'car'))
