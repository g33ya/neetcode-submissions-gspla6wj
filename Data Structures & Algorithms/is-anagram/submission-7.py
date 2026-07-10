class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        - anagrams = requires sorting
        - relationship between two data items -> HashMap
        - idea: create a HashMap of each string, equate and return result
            - HashMap contains count of each char in the given string
        '''

        mapS = {}
        mapT = {}

        for char in s:
            mapS[char] = mapS.get(char, 0) + 1
        for char in t:
            mapT[char] = mapT.get(char, 0) + 1
        
        return mapS == mapT

        
