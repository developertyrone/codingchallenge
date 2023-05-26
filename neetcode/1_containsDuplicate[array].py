class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        history = set()
        result = False
        for n in nums:
            if n not in history:
                history.add(n)
            else:
                return True
        return result