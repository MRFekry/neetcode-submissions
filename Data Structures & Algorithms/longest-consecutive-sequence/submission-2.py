class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        sorted_set = sorted(set(nums))
        counter = 1
        result = 1

        for i in range(len(sorted_set)):
            if i <= (len(sorted_set) - 2) and sorted_set[i + 1] - sorted_set[i] == 1:
                counter += 1
            elif result >= counter:
                counter = 1
            else:
                result = counter
                counter = 1
        
        return result