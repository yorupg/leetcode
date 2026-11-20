class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last = {}

        for i, number in enumerate(nums):
            if (number in last and i - last[number] <= k):
                return True

            last[number] = i
        

        return False