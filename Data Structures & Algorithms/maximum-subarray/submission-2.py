class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if all(n < 0 for n in nums):
            return max(nums)        
        if all(n >= 0 for n in nums):
            return sum(nums)

        result = 0
        for i in range(len(nums)):
            if nums[i] > result:        
                result = nums[i]
            summ = nums[i]
            for j in range(i + 1, len(nums)):
                summ += nums[j]
                if (summ > result):
                    result = summ
                j += 1
            i += 1

        return result