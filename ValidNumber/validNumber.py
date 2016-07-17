import re

class Solution(object):
    _dot_number=0

    def isN(self, s):
        if s=='':
            return False
        for c in s:
            if str.isdigit(str(c)):
                pass
            else:
                return False
        return True


    def isDot(self, s):
        index=s.find('.')
        if index==-1 or index-1==len(s):
            return self.isN(s)
        else:
            return self.isN(s[:index]) and self.isN(s[index+1:])

    def isENumber(self, s):
        s=s.strip()
        index=s.find('e')
        if index==-1 or index-1==len(s):
            return self.isDot(s)
        else:
            return self.isDot(s[:index]) and self.isDot(s[index+1:])


    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isENumber(s)