class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp = set(nums)

        return len(temp) < len(nums)
    
        """
        seen = set()
        
        for number in nums:
            if number in seen:
                return True
            seen.add(number)
                
        return False
        """