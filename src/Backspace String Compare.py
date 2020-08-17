import itertools

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(s):
            skip = 0
            for x in reversed(s):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


t = Solution()
print(t.backspaceCompare("ab##", "c#d#"))
