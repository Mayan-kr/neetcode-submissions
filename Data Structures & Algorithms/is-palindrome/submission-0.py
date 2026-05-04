class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s=''
        for char in s:
            if char.isalnum():
                cleaned_s += char.lower()
        return cleaned_s==cleaned_s[::-1]
         