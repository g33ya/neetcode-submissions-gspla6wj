class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        HashSet/HashMap: HashMap DICT
        Key/Value: sorted anagram, [unsorted anagrams]
        If-condition: If sorted anagram in map, append unsorted anagram
        '''

        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        
        group_anagrams = []

        for anagrams in anagrams.values():
            group_anagrams.append(anagrams)
        
        return group_anagrams