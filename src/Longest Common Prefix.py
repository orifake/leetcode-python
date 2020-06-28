from typing import List


class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     prefix = []
    #     for x in zip(*strs):
    #         if len(set(x)) == 1:
    #             prefix.append(x[0])
    #         else:
    #             break
    #     return "".join(prefix)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]

                if len(prefix) == 0:
                    return ""
        return prefix


t = Solution()
print(t.longestCommonPrefix(["flower", "flow", "flight"]))
