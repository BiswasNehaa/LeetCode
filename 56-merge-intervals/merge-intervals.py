class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        intervals.sort()
        
        merged=[intervals[0]]

        for curr in intervals[1:]:
            last=merged[-1]

            if curr[0]<=last[1]:
                last[1]=max(curr[1],last[1])
            
            else:
                merged.append(curr)
        return merged