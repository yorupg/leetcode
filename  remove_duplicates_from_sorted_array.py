class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1

        for number in range(1, len(nums)):
            if nums[number] != nums[k-1]:
                nums[k] = nums[number]
                k += 1
        return k