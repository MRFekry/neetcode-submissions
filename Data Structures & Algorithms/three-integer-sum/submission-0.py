class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        sortedNums = sorted(nums)
        result = []

        for i, num in enumerate(sortedNums):
            if i > 0 and num == sortedNums[i - 1]:
                continue
            
            l, r = i + 1, len(sortedNums) - 1

            while l < r:
                sumR = num + sortedNums[l] + sortedNums[r]
                if sumR > 0:
                    r -= 1
                elif sumR < 0:
                    l += 1
                else:
                    result.append([num, sortedNums[l], sortedNums[r]])
                    l += 1
                    while sortedNums[l] == sortedNums[l - 1] and l < r:
                        l += 1
        
        return result