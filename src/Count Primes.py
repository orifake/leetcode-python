class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:  # 注意审题边界条件,是小于n,不包括n
            return 0  # 注意 数组越界的情况

        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5) + 1):  # 在选择除数时候的一个小技巧.大于一半的数是不可能做除数的
            if primes[i]:
                primes[i * i:n:i] = [0] * (
                    (n - 1) // i - i + 1)  # 用埃氏筛法, 将每一个不是素数的数筛选掉.大大减少除法的数量.
        return sum(primes)


t = Solution()
print(t.countPrimes(499979))