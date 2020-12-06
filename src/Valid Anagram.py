import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


t = Solution()
print(t.isAnagram('anagram', 'nagaram'))
print(t.isAnagram('rat', 'car'))
