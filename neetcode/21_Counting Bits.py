class Solution:
    def countBits(self, n: int) -> List[int]:
        # Solution 1
        # result = []
        # for i in range(0,n+1):
        #     count = 0
        #     while i:
        #         i = i & (i-1)
        #         count +=1
        #     result.append(count)
        # return result
        # Solution 2
        result = [0]
        offset = 1
        for i in range(1, n+1):
            offset = offset * 2 if offset * 2 == i else offset
            result.append(1 + result[i-offset])

        return result
