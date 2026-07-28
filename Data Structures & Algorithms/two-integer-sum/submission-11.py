class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        
        left = 0
        while left < len(nums):
            right = left + 1
            while right < len(nums):
                if nums[left] + nums[right] == target:
                    return [left, right]
                right += 1
            left += 1

        return []