class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store sorted list of a string as a key, index as its value
        sorted_strs = defaultdict(list)

        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in sorted_strs:
                sorted_strs[sorted_str].append(strs[i])
            else:
                sorted_strs[sorted_str].append(strs[i])

        final_list = []
        for key in sorted_strs:
            final_list.append(sorted_strs[key])

        return final_list