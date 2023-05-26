class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = re.sub(r'[^a-zA-Z0-9]', '', s)
        filtered = filtered.lower()
        if filtered == filtered[::-1]:
            return True
