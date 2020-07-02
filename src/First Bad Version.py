# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo,hi = 1,n
        while lo < hi:
            mid = int((lo + hi)/2)
            res = isBadVersion(mid)
            if res:
                hi = mid
            else:
                lo = mid + 1
        return lo