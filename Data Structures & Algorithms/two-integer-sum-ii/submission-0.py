class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []

        i = 0
        j = len(numbers) - 1

        while i != j:
            sumResult = numbers[i] + numbers[j]
            if sumResult == target:
                return [i + 1, j + 1]
            
            if sumResult > target:
                j -= 1            
            elif sumResult < target:
                i += 1            
        
        return []
