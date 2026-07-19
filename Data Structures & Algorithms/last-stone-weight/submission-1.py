import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while(len(stones) > 1):
            largest1 = heapq.heappop_max(stones)
            largest2 = heapq.heappop_max(stones)
            heapq.heappush_max(stones, largest1 - largest2)
        
        return heapq.heappop(stones)