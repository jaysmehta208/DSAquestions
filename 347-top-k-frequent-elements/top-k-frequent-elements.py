class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        s = list(d.items())
        h = []
        for i in range(len(s)):
            heapq.heappush(h, (-1 * s[i][1], s[i][0]))
        l = []
        for i in range(k):
            l.append(heapq.heappop(h)[1])
        return l