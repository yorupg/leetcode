class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and  nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break

            while l < r:
                current_sum = nums[i] + nums[r] + nums[l]

                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
        return res