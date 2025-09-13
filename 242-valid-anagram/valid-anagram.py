class Solution(object):
    def isAnagram(self, s, t):
        str1 = {}
        str2 = {}

        for i in s:
            if i not in str1:
                str1[i] = 1
            else:
                str1[i] += 1

        for j in t:
            if j not in str2:
                str2[j] = 1
            else:
                str2[j] += 1

        return str1 == str2