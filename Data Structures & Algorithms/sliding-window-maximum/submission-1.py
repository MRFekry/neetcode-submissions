class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            if len(nums) == 0: return []
            if len(nums) == 1: return [nums[0]]
            if k == 1: return nums
            res = []
            for i, n in enumerate(nums):
                rp = i + k
                if rp <= len(nums):
                    res.append(max(nums[i:rp]))
                if rp == len(nums):
                    break
            return res


