class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=0
        n=len(nums)

        if n==0:
            return []
        
        result=[]

        while i< n:
            j=i+1

            while j<n:
                if nums[j-1]+1 == nums[j]:
                    j+=1
                else:
                    break
                
            if(j-i==1):
                result.append(str(nums[i]))
            else:
                result.append(str(nums[i]) + "->" + str(nums[j-1]))
                
            i=j
        return result