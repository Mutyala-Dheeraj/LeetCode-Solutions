class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s.strip()
        stack = []
        pairs = {'(': ')','[': ']','{': '}'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                s1 = stack[-1]
                if i == pairs[s1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
