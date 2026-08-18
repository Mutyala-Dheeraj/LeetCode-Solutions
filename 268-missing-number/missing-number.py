class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        f = n*(n+1)//2
        s = 0
        for i in nums:
            s = s + i
        r = f - s
        return r     