class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        - anagrams
        - count hashmap for each string -> equality check at end
        '''

        hashS = {}
        hashT = {}

        for c in s:
            hashS[c] = hashS.get(c, 0) + 1

        for c in t:
            hashT[c] = hashT.get(c, 0) + 1

        return hashS == hashT
        
