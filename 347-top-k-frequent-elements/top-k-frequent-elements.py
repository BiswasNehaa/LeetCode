from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count=Counter(nums)
        top_k=count.most_common(k)

        res=[]
        for num,freq in top_k:
            res.append(num)
        
        return res