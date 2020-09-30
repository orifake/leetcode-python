import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)

        return min(cnt.get('b', 0), cnt.get('a', 0), int(cnt.get('l', 0) / 2),
                   int(cnt.get('o', 0) / 2), cnt.get('n', 0))


t = Solution()
print(t.maxNumberOfBalloons('balon'))
print(t.maxNumberOfBalloons('loonbalxballpoon'))
