class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = {}

        for i, number in enumerate(nums):
            need = target - number

            if need in res:
                return [res[need], i]
          
            res[number] = i