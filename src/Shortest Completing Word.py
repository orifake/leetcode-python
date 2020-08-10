from typing import List
import re
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str,
                               words: List[str]) -> str:
        regex = re.compile('[^a-zA-Z]')
        license = regex.sub('', licensePlate)
        counter1 = Counter(license.lower())
        res = ''
        for word in words:
            if self.count(counter1, word):
                if res == '' or len(word) < len(res):
                    res = word
        return res

    def count(self, counter1, word):
        counter2 = Counter(word)
        counter2.subtract(counter1)
        return all([c >= 0 for c in counter2.values()])