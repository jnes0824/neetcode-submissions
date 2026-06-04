class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        arr = []
        for num, count in d.items():
            arr.append([count, num])
        arr.sort(key = lambda x: x[0])

        res = []
        for i in range(k):
            num = arr.pop()[1]
            res.append(num)
        return res