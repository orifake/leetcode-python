class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        ans = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[int(i / 2)]
            else:
                nums[i] = nums[int(i / 2)] + nums[int(i / 2) + 1]
            ans = max(ans, nums[i])
        return ans


t = Solution()
print(t.getMaximumGenerated(7))
