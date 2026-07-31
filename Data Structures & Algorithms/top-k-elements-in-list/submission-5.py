class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        most frequent -> hashmap
        count hashmap

        loop through k times, returning key with max count value each time
        '''

        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        

        top_k = []
        for i in range(k):
            max_element = max(frequency, key=frequency.get)
            top_k.append(max_element)
            frequency[max_element] = -1
        
        return top_k
