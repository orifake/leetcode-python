from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = 'qwertyuiopasdfghjklzxcvbnm'
        ans = []
        for word in words:
            if len(word) == 1:
                ans.append(word)
                continue
            prev = -1
            for i, char in enumerate(word):
                index = keyboard.find(char.lower())
                if index < 10:
                    curr = 0
                elif index > 18:
                    curr = 2
                else:
                    curr = 1

                if i == 0:
                    prev = curr
                elif prev != curr:
                    break
                elif i == len(word) - 1:
                    ans.append(word)

        return ans


t = Solution()
print(t.findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(t.findWords(["a", "b"]))
