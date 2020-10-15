import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        ans = 0
        largest = 0
        dic = collections.defaultdict(int)
        for i in range(1, n + 1):
            num = i % 10 + (i // 10) % 10 + (i // 100) % 10 + (
                i // 1000) % 10 + i // 10000
            dic[num] += 1
            if dic[num] > largest:
                largest = dic[num]
                ans = 1
            elif dic[num] == largest:
                ans += 1
        return ans


t = Solution()
print(t.countLargestGroup(13))