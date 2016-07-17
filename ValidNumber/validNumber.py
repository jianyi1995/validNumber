class Solution(object):
    _dot_number=0
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False

        s = s.strip()
        if s is None:
            return False
        for c in s:
            if str.isdigit(c):
                pass
            elif c=='.':
                self._dot_number+=1
                if self._dot_number>1:
                    return False
            else:
                return False
        return True