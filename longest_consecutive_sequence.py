class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_count = 0

        seen = set(nums)

        for num in seen:
            k = 1
            if num - 1 not in seen:
                while num + 1 in seen:
                    num += 1
                    k += 1
                max_count = max(k, max_count)
        
        return max_count