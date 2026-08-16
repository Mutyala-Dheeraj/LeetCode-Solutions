class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            num = -(x)
            reverse = 0
            while num>0:
                r= num % 10
                reverse = reverse *10 +r
                num = num // 10
            if reverse > 2**31-1 or reverse < -2**31:
                return 0
            else:
                return -(reverse)
        else:
            s = str(x)
            rev = s[::-1]
            i = int(rev)
            if i > 2**31-1 or i < -2**31:
                return 0
            else:
                return i

        