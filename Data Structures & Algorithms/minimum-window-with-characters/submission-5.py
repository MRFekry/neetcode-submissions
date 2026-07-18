from collections import defaultdict, Counter, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return t
        if t == "": return ""
        
        tCounter = Counter(t)
        window = defaultdict(int)
        have = 0
        need = len(tCounter)
        substring = deque([])
        result = ""

        for c in s:
            if c in t:
                window[c] += 1
                substring.append(c)
                if window[c] == tCounter[c]:
                    have += 1
                if have == need:
                    while substring[0] not in window or window[substring[0]] > tCounter[substring[0]]:
                        if substring[0] in window:
                            window[substring[0]] -= 1
                        substring.popleft()
                    if result == "" or len(substring) < len(result):
                        result = "".join(substring)
                    left_char = substring[0]
                    window[left_char] -= 1
                    substring.popleft()
                    if window[left_char] < tCounter[left_char]:
                        have -= 1
            else:
                substring.append(c)
        
        return result

                        