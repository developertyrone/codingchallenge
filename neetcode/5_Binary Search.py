from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            cur = (left + right) // 2
            if nums[cur] == target:
                return cur
            elif nums[cur] > target:
                right = cur - 1
            elif nums[cur] < target:
                left = cur + 1
        return -1

#[-1,0,3,5,9,12]
#https://leetcode.com/problems/binary-search/editorial/

