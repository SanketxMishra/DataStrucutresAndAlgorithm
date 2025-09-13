class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted((nums))
        d = {}
        for idx , val in enumerate(temp):
            if val not in d:
                d[val]=idx
        out = []
        for i in nums:
            out.append(d[i])
        return out
