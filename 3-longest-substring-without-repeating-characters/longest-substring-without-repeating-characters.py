class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = ""
        l = []
        for i in s:
            if i not in st:
                st = st + i
                l.append(len(st))
            else:
                 st = st[st.index(i) + 1:] + i
                 l.append(len(st))
        return max(l) if l else 0


        