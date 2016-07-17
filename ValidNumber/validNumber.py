class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False

        s = s.strip()
        if '.' not in s and 'e' not in s:
            try:
                result = int(s)
                return True
            except:
                return False
