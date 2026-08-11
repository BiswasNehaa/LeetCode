class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand=0
        count=0

        for i in nums:
            if count==0:
                cand=i
            
            if i==cand:
                count+=1
            else:
                count -=1
        return cand

