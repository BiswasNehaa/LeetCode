class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_num=nums[0]
        max_sum=nums[0]

        for i in range (1, len(nums)):
            curr_num=max(nums[i],curr_num+nums[i])
            max_sum=max(max_sum,curr_num)
        return max_sum