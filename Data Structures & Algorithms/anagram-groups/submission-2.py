class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        sortedStrs = [ "".join(sorted(s)) for s in strs ]

        for index in range(len(strs)):
            word = strs[index];
            signature = sortedStrs[index];

            if signature in anagrams:
                anagrams[signature].append(word)
            else:
                anagrams[signature] = [word]

        return list(anagrams.values())