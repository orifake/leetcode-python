class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def Eluer_filter(n):
            """
            欧拉筛法, 每次用质数因子去筛，即当前的如果是合数的话就不用该数作为因子，
             因为以它作为因子得到的数之前肯定也能得到
            """
            count = 0
            array = [False for i in range(n + 1)]
            array[1] = True
            index = 2
            while index < len(array):
                if array[index]:
                    index += 1
                    continue
                for i in range(index * 2, n + 1, index):
                    array[i] = True
                index += 1

            for i in range(1, len(array)):
                if not array[i]:
                    count += 1
            return count

        def fac(n):
            return 1 if n <= 1 else n * fac(n - 1)

        prime = Eluer_filter(n)
        non_prime = n - prime
        return (fac(prime) * fac(non_prime)) % (pow(10, 9) + 7)


t = Solution()
print(t.numPrimeArrangements(5))