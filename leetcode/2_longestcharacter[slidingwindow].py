# Given a string s, find the length of the longestsubstring without repeating characters.

# Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        for i in range(len(s), 0, -1):
            for x in range(len(s)-i+1):
                wth = len(s[x:i+x])
                if (wth == len(set(s[x:i+x]))):
                    return wth



# Sliding Window
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cans = 0
        cache = set()
        left = 0

        for n in range(len(s)):
            while s[n] in cache:
                cache.remove(s[left])
                left += 1
            ans = max(ans, n-left+1)
            cache.add(s[n])

        return ans


# Better Sliding Windows
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


# #######
# Tips
#
# All previous implementations have no assumption on the charset of the string s.
#
# If we know that the charset is rather small, we can mimic what a HashSet/HashMap does with a boolean/integer array as direct access table.
# Though the time complexity of query or insertion is still O(1)O(1)O(1), the constant factor is smaller in an array than in a HashMap/HashSet.
# Thus, we can achieve a shorter runtime by the replacement here.
#
# Commonly used tables are:
#
#     int[26] for Letters 'a' - 'z' or 'A' - 'Z'
#     int[128] for ASCII
#     int[256] for Extended ASCII

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index is not None and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res
##
# For this implementation, the space complexity is fixed to O(m)O(m)O(m) while the time complexity keeps unchanged.
# mmm is the size of the charset.
