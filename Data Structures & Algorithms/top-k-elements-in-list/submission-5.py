class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = sorted(Counter(nums).items(), key= lambda x: x[1], reverse=True)
        return [t[0] for t in counter][:k]
        