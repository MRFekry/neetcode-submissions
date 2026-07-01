class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        dic = dict()
        for num in nums:
            if num in dic:
                return True
            dic[num] = None
        return False

