class Solution:
    def maximum69Number(self, num: int) -> int:
        return str(num).replace('6', '9', 1)


t = Solution()
print(t.maximum69Number(9669))
