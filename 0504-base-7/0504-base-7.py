class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        sign = ""
        if num < 0:
            sign = "-"
            num = -num
        res = ""
        while (num>0):
            r=num%7
            res = str(r) + res
            num = num / 7
        return sign + res