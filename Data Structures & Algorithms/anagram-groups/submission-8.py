class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - anagrams -> hashmap
        - key: sorted anagram, value: list of unsorted anagrams
        '''
        anagramMap = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagramMap[sorted_s].append(s)
        
        grouped_anagrams = []

        for anagram in anagramMap.values():
            grouped_anagrams.append(anagram)
        return grouped_anagrams
        