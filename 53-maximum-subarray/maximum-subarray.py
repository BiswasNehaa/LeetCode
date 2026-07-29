class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        maxi=nums[0]
        for i in range(len(nums)):
            total=total+nums[i]
            maxi=max(maxi,total)
            if total<0 :
                total=0
        return maxi