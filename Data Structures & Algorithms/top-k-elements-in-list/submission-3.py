class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        count hashmap
        - key: list element, value: count
        '''
       
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1


        top_k = []
        
        while k > 0:
            most_frequent = max(counts, key=counts.get)
            top_k.append(most_frequent)
            counts[most_frequent] = -1
            k = k - 1
        
        return top_k
