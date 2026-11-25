class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counts = {0: 1}
        current_sum = 0
        res = 0

        for num in nums:
            current_sum += num

            if (current_sum - k) in counts:
                res += counts[current_sum - k]

            counts[current_sum] = counts.get(current_sum, 0) + 1
            
        return res