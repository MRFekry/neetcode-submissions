class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            k = (l+r) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            if hrs > h:
                l = k + 1
            elif hrs <= h:
                r = k - 1
                result = min(result, k)
        return result
            
