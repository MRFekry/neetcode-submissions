class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s.isspace() or len(s) == 1:
            return 1

        cDic = {}
        longestS = ''
        startIndex = 0
        subS = ''

        for i, c in enumerate(s):
            if c not in cDic:
                cDic[c] = cDic.get(c, i)
                subS += c
                if i == len(s) - 1:
                    longestS = subS
            else:
                if len(subS) > len(longestS):
                    longestS = subS
                startIndex = max(startIndex, cDic[c] + 1)
                cDic[c] = i
                subS = s[startIndex:i + 1]

        return len(longestS)

