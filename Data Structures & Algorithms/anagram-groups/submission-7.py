class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        hashmap of key: sorted anagram with value of list unsorted anagram
        append to final list
        '''

        anagrams = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            anagrams[sorted_str].append(s)
        
        final_list = []

        for val in anagrams.values():
            final_list.append(val)

        return final_list