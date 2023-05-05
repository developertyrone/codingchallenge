# Given a string s, return the longest palindromic substring in s.

# brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        anslen = 0
        ans = 0
        for n in range(len(s)):
            for m in range(n+1, len(s)+1):
                subs = s[n:m]
                if len(subs) > anslen and subs == subs[::-1] :
                    anslen = m-n
                    ans = subs
                # print(s[n:m], s[n:m][::-1], m-n)
        return ans


# better way
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (s is None or len(s) < 1):
            return ""
        start, end = 0, 0
        for n in range(len(s)):
            ans1 = self.expandToEdge(s, n, n)
            ans2 = self.expandToEdge(s, n, n+1)
            lenth = max(ans1, ans2)
            if (lenth > end - start) :
                start = n - int ((lenth - 1) / 2)
                end = n + int (lenth / 2)
        return s[start:end+1]

    def expandToEdge(self, s: str, left: int, right: int):
        l, r = left, right
        while (l >= 0 and r < len(s)) and s[l] == s[r]:
            l -= 1
            r += 1
        return r-l-1