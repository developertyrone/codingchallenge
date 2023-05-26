class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1
        while digits:
            cur = digits.pop(-1)

            val = (cur + carry) % 10
            carry = (cur + carry) // 10
            result.insert(0, val)

        if carry > 0:
            result.insert(0, carry)

        return result