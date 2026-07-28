from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = defaultdict(int)

        for c in s:
            sdic[c] += 1
        
        for c in t:
            sdic[c] -= 1
        
        return all(v == 0 for v in sdic.values())
        