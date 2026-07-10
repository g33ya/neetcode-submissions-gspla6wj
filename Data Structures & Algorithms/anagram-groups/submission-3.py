class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - anagram = sorting?
        - idea: create a HashMap with the SORTED anagram as the key, unsorted
        anagram(s) as the value (list).
            - append values to a final list, return
        '''

        anagrams = defaultdict(list)
        
        for string in strs:
            sorted_string = "".join(sorted(string))
            anagrams[sorted_string].append(string)
        
        final_list = []

        for value in anagrams.values():
            final_list.append(value)

        return final_list