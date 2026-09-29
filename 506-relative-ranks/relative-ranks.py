class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        a = sorted(score,reverse=True)
        dic = {}
        for i in a:
            if a.index(i) == 0:
                dic[i] = "Gold Medal"
            elif a.index(i) == 1:
                dic[i] = "Silver Medal"
            elif a.index(i) == 2:
                dic[i] = "Bronze Medal"
            else:
                dic[i] = str(a.index(i)+1)
        l = []
        for i in score:
            l.append(dic[i])
        return l


            

