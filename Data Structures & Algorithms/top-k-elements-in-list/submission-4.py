class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        count hashmap
        - key: list element, value: count
        '''
       
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        top_k = []

        while k > 0:
            top = max(count, key=count.get)
            top_k.append(top)
            count[top] = -1
            k -= 1
        
        return top_k


