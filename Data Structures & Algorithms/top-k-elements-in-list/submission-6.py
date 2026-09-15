class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        top_k = []
        for i in range(k):
            max_freq = max(counts, key=counts.get)
            top_k.append(max_freq)
            counts[max_freq] = -1

        return top_k