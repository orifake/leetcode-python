from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_map = defaultdict(int)
        bulls_count = 0
        cows_count = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls_count += 1
                # 下次循环时跳过
                guess = guess[:i] + 'p' + guess[i + 1:]
            else:
                count_map[secret[i]] += 1

        for i in range(len(secret)):
            if guess[i] != 'p' and count_map[guess[i]] > 0:
                cows_count += 1
                count_map[guess[i]] -= 1

        return str(bulls_count) + "A" + str(cows_count) + "B"


t = Solution()
print(t.getHint('1123', '0111'))
