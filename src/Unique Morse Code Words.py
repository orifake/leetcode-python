from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]

        seen = {
            "".join(MORSE[ord(c) - ord('a')] for c in word)
            for word in words
        }

        return len(seen)


t = Solution()
print(t.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))