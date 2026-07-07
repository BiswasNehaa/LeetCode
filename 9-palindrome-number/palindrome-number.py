class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x=str(x)
        start=0
        end= len(str_x)-1
        while start<end:
            if str_x[start] != str_x[end]:
                return False
            else:
                start=start+1
                end= end-1
        return True