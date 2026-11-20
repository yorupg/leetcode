class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """ var 1
        seen = set()

        for number in nums:
            
            if number in seen:
                seen.remove(number)
            else:
                seen.add(number)
        return seen.pop()"""

        res = 0

        for number in nums:
            res ^= number
        
        return res