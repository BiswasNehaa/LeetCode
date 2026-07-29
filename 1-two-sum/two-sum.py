class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        for i in range (len(nums)):
            rem=target-nums[i]
            if rem  in  hash_map:
                return [hash_map[rem],i]
            hash_map[nums[i]]=i