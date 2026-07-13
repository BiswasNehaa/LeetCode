class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_s="".join(i.lower() for i in s if i.isalnum())
        start=0
        end=len(clean_s)-1
        while start<end:
            if clean_s[start]!=clean_s[end]:
                return False
            else:
                start=start+1
                end=end-1
        return True