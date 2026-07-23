class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        1. sort: by END (non-overlapping)
        2. prior info to track?
            - 
        '''

        intervals.sort(key = lambda i : i[1]) # sort by end
        non_overlap = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = non_overlap[-1][1]
            if lastEnd <= start:
                non_overlap.append([start, end])
        
        return len(intervals) - len(non_overlap)