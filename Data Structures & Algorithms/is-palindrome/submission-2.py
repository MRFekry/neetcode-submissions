class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 0: return False
        if len(s) == 1: return True        
        s = "".join(c for c in s if c.isalnum()).lower()
        left, right = 0, len(s) - 1
        while left != int(len(s) / 2):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


        