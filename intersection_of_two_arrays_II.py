class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = {}
        res = []
        small = nums1
        large = nums2
        
        if len(nums1) > len(nums2):
            small = nums2
            large = nums1
        
        for num in small:
            counts[num] = counts.get(num, 0) + 1

        for num in large:
            if num in counts:
                if counts[num] > 0:
                    res.append(num)
                    counts[num] -= 1

        return res
            