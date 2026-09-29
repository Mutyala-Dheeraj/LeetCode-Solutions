class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l = []
        for i in list1:
            for j in list2:
                if i == j:
                    l.append(i)
        k= {}
        for i in l:
            ind = list1.index(i)+list2.index(i)
            k[i] = ind
        minimum = min(k.values())

        result= [] 
        for i in k:
            if k[i] == minimum:
                result.append(i)
        return result

            
        