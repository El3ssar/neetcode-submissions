from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for elem in nums:
            counts[elem] += 1
        decrease_sorted = sorted(counts, key=counts.get, reverse=True)
        return decrease_sorted[:k]
