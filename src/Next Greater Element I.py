from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:
        m = {}
        st = []
        ans = []
        for x in nums2:
            while len(st) and st[-1] < x:
                m[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(m.get(x, -1))

        return ans


t = Solution()
print(t.nextGreaterElement([2, 4], [1, 2, 3, 4]))
