from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        A_sum = sum(A)
        if A_sum % 3:
            return False

        left, right = 0, len(A) - 1
        leftSum, rightSum = A[left], A[right]

        while left + 1 < right:
            if leftSum == A_sum / 3 and rightSum == A_sum / 3:
                return True
            if leftSum != A_sum / 3:
                left += 1
                leftSum += A[left]
            if rightSum != A_sum / 3:
                right -= 1
                rightSum += A[right]

        return False


t = Solution()
print(t.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
