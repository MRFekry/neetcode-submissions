class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x_index = 0
        for x in nums:
            y_index = 0
            for y in nums:
                if x_index == y_index:
                    y_index = y_index + 1
                    continue
                if x + y == target:
                    return [x_index, y_index]
                y_index = y_index + 1
                continue
            x_index = x_index + 1
        