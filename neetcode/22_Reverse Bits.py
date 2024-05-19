# https://www.youtube.com/watch?v=-5z9dimxxmI
# https://leetcode.com/problems/reverse-bits
# https://www.youtube.com/watch?v=UcoN6UjAI64&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=OTY3MTQ&feature=emb_imp_woyt

class Solution:
    def reverseBits(self, n: int) -> int:
        # result = 0
        # bit = 31
        # while n:
        #     result += (n % 2) * pow(2,bit)
        #     n = n >> 1
        #     bit -= 1
        # return result
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31-i))
        return result