class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i = 0
        for lh in heights:
            j = 0
            for rh in heights:
                if i >= j:
                    j += 1
                    continue
                min, area, wide = 0, 0, j - i
                if lh <= rh:
                    min = lh
                elif rh < lh:
                    min = rh
                area = min * wide
                if area > result:
                    result = area
                j += 1
            i += 1
        return result
                    