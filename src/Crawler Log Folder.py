from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for cmd in logs:
            if cmd == "../":
                if depth > 0:
                    depth -= 1
            elif cmd != "./":
                depth += 1

        return depth


t = Solution()
print(t.minOperations(["d1/", "d2/", "../", "d21/", "./"]))
