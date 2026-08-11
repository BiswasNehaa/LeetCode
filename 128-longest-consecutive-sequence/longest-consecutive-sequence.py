class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=1
        longest=1
        n=len(nums)
        if n==0:
            return 0
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1]:
                count+=1
            else:
                count=1

            longest=max(longest,count)
        return longest