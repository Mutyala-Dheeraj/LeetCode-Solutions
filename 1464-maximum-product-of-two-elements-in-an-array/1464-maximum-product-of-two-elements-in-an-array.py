class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = 0
        m2 = 0
        for i in nums:
            if i > m1:
                m2 = m1
                m1 = i
            elif i > m2:
                m2 = i
        return (m1-1)*(m2-1)


        