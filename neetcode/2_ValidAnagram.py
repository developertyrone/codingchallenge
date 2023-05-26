from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = Counter(s)
        right = Counter(t)
        if left == right:
            return True
        else:
            return False
