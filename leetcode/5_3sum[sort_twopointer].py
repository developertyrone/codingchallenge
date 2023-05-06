from typing import List
#https://betterexplained.com/articles/easy-permutations-and-combinations/
#https://www.geeksforgeeks.org/permutation-and-combination-in-python/

class Solution:
    # Solution 1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            print (i,a)
            ## this handle for the
            if i > 0 and a == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                target = a + nums[l] + nums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

    # Solution 2
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            self.twoSum(nums, i+1, len(nums)-1, -a, res)
        return res

    def twoSum(self, nums: List[int], l: int, r: int, target: int, res: List[List[int]]):
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([-target, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

    # Solution 3
    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, neg, pos, zero = [], [], [], []
        for i in nums:
            if (i < 0):
                neg.append(i)
            elif (i > 0):
                pos.append(i)
            else:
                zero.append(i)

        # for zero case
        if (len(zero) >= 3):
            res.append([0, 0, 0])

        # for pure negative or positive list
        if (len(neg) == 0 or len(pos) == 0):
            return res

        # for negative and positive list



if __name__ == "__main__":
    s = Solution()
    result = s.threeSum([-1,0,1,2,-1,-4])
    print(result)
    result = s.threeSum([0,0,0,0])
    print(result)
    result = s.threeSum([0, 0, 0])
    print(result)
    result = s.threeSum([0, 0, 1])
    print(result)
    result = s.threeSum2([-1,0,1,2,-1,-4])
    print(result)