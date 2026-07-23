class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if all(n < 0 for n in nums):
            return max(nums)        
        if all(n >= 0 for n in nums):
            return sum(nums)

        i, currSum, maxSum = 0, 0, nums[0]
        while i < len(nums):
            currSum = max(currSum, 0)
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            i += 1
        return maxSum