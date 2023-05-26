import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [x * -1  for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            last, last2 = heapq.heappop(stones), heapq.heappop(stones)
            diff = last-last2
            if diff != 0:
                heapq.heappush(stones,diff)

        return 0 if len(stones) == 0 else stones[0] * -1