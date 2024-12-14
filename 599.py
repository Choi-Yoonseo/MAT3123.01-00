class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        dic = {}

        for x, val in enumerate(list1):
            if val in list2:
                dic[val] = x + list2.index(val)

        dic = sorted(dic.items(), key=lambda x: x[1])
        minimum = dic[0][1]
        return [x[0] for x in dic if x[1]==minimum]

