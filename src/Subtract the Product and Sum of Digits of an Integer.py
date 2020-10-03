class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_n = 0
        prod = 1

        while n:
            sum_n += n % 10
            prod *= n % 10
            n = int(n / 10)

        return prod - sum_n


t = Solution()
print(t.subtractProductAndSum(234))