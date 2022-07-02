from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for key, val in c.items():
            if len(h) < k:
                heapq.heappush(h, (val, key))
            elif h[0][0] < val:
                heapq.heappushpop(h, (val, key))
        return [v for (_, v) in h]
    def topKFrequentv2(self, nums: List[int], k: int) -> List[int]:
        return [fst for (fst, _) in Counter(nums).most_common(k)]