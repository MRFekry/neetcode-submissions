class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}

        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        
        top_k = []
        sorted_num_counts = sorted(num_counts.items(), key=lambda item: item[1], reverse=True)
        
        for index in range(k):
            top_k.append(sorted_num_counts[index][0])
        
        return top_k
        