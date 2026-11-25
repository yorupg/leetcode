class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0 ) + 1

        backet = [ [] for i in range(max(counts.values())+ 1)]

        for count in counts:
            backet[counts[count]].append(count)
           
        res = []
        
        for i in range(len(backet) - 1, 0, -1):
            for n in backet[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
