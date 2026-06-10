class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        
        n = len(s)
        for i in range(n):
            if s[i] != s[-i - 1]:
                return False
        return True