class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        new_str = ''.join(chars)
        return new_str == new_str[::-1]