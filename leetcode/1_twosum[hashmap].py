# #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List

# o(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for x in range(i+1, len(nums)):
                if(target == nums[i] + nums[x]):
                    return [i,x]

# o(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(0, len(nums)):
            check = target - nums[i]
            if check in cache:
                return [i, cache[check]]
            else:
                cache[nums[i]] = i