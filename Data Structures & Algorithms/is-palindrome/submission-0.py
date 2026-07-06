class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        if len(s) == 1:
            return True

        all_alnum = "".join(c for c in s if c.isalnum()).lower()
        
        for i in range(len(all_alnum)):
            if i == int((len(all_alnum)/2) + 1):
                break
            if all_alnum[i] != all_alnum[(len(all_alnum) - i) - 1]:
                return False
        
        return True


        