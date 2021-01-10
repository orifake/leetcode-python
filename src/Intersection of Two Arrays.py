from typing import List


class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(), nums2.sort()
        res = []

        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                if not res or res[-1] != nums1[it1]:
                    res += nums1[it1],
                it1 += 1
                it2 += 1

        return res


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)


t = Solution()
print(t.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
