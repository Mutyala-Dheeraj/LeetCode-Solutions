class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}
        for i in arr:
            freq[i] = arr.count(i)
        m = 0
        c = 0  
        for j in freq:
            if j == freq[j]:
                c = j 
                m = max(c,m)
            else:
                c = 0
        if m:
            return m
        else:
            return -1

        