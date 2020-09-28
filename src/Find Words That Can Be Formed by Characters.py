from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for word in words:
            c = collections.Counter(word)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(word)

        return ans


t = Solution()
print(t.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
