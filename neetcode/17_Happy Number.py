class Solution:
    def isHappy(self, n: int) -> bool:

        histories = []
        while n != 1:
            strnum = str(n)
            n = 0
            for i in strnum:
                n += pow(int(i), 2)
            if n in histories:
                return False
            else:
                histories.append(n)

        return True
