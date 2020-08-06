from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        self.size = len(self.pool)
        heapq.heapify(self.pool)
        print(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)

        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

kthLargest = KthLargest(3, [4,5,8,2])
print(kthLargest.add(3))
