class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        else:
            n = s+s
            if goal in n:
                return True
            else:
                return False
    