class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - HashMap
        - SORTING! 
        - key: sorted anagram, value: unsorted anagram
        - print("".join(sorted("pots")))
        '''

        anagrams = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string].append(string)
        
        print(anagrams)

        final_list = []

        for value in anagrams.values():
            final_list.append(value)

        return final_list
