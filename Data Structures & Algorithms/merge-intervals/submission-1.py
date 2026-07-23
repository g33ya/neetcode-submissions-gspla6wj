class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        1. sort by start/end: START
        2. initialize output array w/ first element
        3. loop through intervals [1:] (for start, end in intervals[1:])
          comparing most recently added interval ([-1]) in outputs to 
          current item 
        '''

        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output