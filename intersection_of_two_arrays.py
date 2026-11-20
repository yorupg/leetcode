class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        res = []

        for number in set1:
            if number in set2:
                res.append(number)

        """res = list(set1 & set2)"""
        return res 