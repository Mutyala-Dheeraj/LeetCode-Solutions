class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        n = len(nums)
        n = len(nums)
        for i in range (0,n-1):
            for j in range (i+1,n):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        if n%2==0:
            return (nums[(n-1)//2]+nums[n//2])/2.0
        else:
            return nums[n//2]

