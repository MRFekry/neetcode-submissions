class Solution:

    def encode(self, strs: List[str]) -> str:
        # add each string in strs to a encoded string followed by its length
        # assuming that no numeric chars in the strs list
        encodedString = ""
        encodedString = "".join(str(len(s)) + '#' + s for s in strs)
        return encodedString

    def decode(self, s: str) -> List[str]:
        # loop over each char in s and add it to string until char is numeric
        # add the string to list of strings
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            strs.append(word)
            i = j + 1 + length
        return strs