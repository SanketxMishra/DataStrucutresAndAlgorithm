class Solution(object):
    def findDisappearedNumbers(self, nums):
        out = []
        dist = set(nums)
        for i in range(1,len(nums)+1):
            if i not in dist:
                out.append(i)
        return out
        