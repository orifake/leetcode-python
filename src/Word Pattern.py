class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_count = {}
        words = str.split()
        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            p = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(p)
            char_word = 'word_{}'.format(w)

            if char_key not in map_count:
                map_count[char_key] = i

            if char_word not in map_count:
                map_count[char_word] = i

            if map_count[char_key] != map_count[char_word]:
                return False

        return True


t = Solution()
print(t.wordPattern("abba", "dog cat cat fish"))
