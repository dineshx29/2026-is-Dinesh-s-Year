class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
        s = ''.join(c.lower() for c in s if c.isalnum())