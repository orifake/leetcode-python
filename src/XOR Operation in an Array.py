class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xorNums(n, start):
            def xorNumsBeginEven(n, start):
                assert (start % 2 == 0)
                # 2*i ^ (2*i+1) = 1
                return ((n // 2) % 2) ^ ((start + n - 1) if n % 2 else 0)

            return start ^ xorNumsBeginEven(
                n - 1, start + 1) if start % 2 else xorNumsBeginEven(n, start)

        return int(n % 2 and start % 2) + 2 * xorNums(n, start // 2)


t = Solution()
print(t.xorOperation(5, 0))
