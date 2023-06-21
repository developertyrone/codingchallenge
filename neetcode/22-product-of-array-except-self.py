# https://leetcode.com/problems/product-of-array-except-self/description/

import numpy


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 _ x 2 x 3 x 4
        # 2 1 x _ x 3 x 4
        # 3 1 x 2 x _ x 4
        # 4 1 x 2 x 3 x _
        # Stupid solution
        # answer = []
        # left = 1
        # for i in range(len(nums)):

        #    temp = nums[0]
        #    nums.pop(0)
        #    answer.append(int(left * numpy.prod(nums)))
        #    left *= temp
        # return answer
        # public solution
        # l, r, n = 1, 1, len(nums) - 1
        # output = [1] * len(nums)

        # for i, j in zip(range(n), range(n, 0, -1)):
        #     l *= nums[i]; r *= nums[j]
        #     output[i + 1] *= l
        #     output[j - 1] *= r

        # return output
        # neet code solution
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans

