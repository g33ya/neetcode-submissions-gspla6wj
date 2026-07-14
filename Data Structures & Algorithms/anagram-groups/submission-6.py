class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - HashMap -> defaultdict
        - key: sorted anagram, value: [ unsorted anagram ]
        - return final list containing values of hashmap
        '''

        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)

        final_list = []

        for anagram in anagrams.values():
            final_list.append(anagram)

        return final_list