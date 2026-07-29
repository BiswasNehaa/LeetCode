class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1={}
        left=0
        right=0
        maxi=0
        n=len(s)
        while right < n:
            if s[right] in dict1:
                left=max(left,dict1[s[right]]+1)
            maxi=max(maxi,right-left+1)
            dict1[s[right]]=right
            right+=1
        return maxi 