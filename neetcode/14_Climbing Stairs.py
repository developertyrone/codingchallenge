from itertools import combinations


class Solution:
    def climbStairs(self, n: int) -> int:

        sums = []
        for i in range(1, n + 1):
            if i > 2:
                sums.append(sums[-1] + sums[-2])
            else:
                sums.append(i)

        return sums[-1]
