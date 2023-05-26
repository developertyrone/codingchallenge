class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        left = []
        conversion = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            # left character
            if c in conversion:
                left.append(conversion[c])
            # right character
            else:
                if len(left) == 0:
                    return False
                elif left[-1] != c:
                    return False
                else:
                    left.pop()

        return not left



