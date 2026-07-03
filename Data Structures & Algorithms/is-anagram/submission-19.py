class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagrams = {}
        index = 0
        for c in s:
            if s[index] in anagrams:
                anagrams[c] += 1
            else:
                anagrams[c] = 1
            if t[index] in anagrams:
                anagrams[t[index]] -= 1
            else:
                anagrams[t[index]] = -1
            index += 1
        for v in anagrams.values():
            if v != 0:
                return False
        return True
        