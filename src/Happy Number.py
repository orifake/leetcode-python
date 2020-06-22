class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(fast)
            fast = self.squareSum(fast)
            if slow == fast:
                break
        return slow == 1

    def squareSum(self, n):
        sum = 0
        while (n > 0):
            sum += int(n % 10) * int(n % 10)
            n /= 10
        return sum


t = Solution()
print(t.isHappy(19))
