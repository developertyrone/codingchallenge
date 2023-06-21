# https://leetcode.com/submissions/detail/975714089/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kele = [[]]  # count, nums
        answer = set()
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

            if len(kele) - 1 >= counter[n]:
                kele[counter[n]].append(n)
            else:
                kele.append([n])

        print(kele)
        for b in range(len(kele) - 1, -1, -1):
            for bi in kele[b]:
                answer.add(bi)
                if len(answer) == k:
                    return list(answer)
