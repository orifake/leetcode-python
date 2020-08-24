from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        return [word for word in count if count[word] == 1]


t = Solution()
print(t.uncommonFromSentences("apple apple", "banana"))
