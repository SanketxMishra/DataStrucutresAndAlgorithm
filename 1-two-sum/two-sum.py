class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for idx, val in enumerate(nums) :
            final = target - val
            if final in dict:
                return [dict[final],idx]
            dict[val] = idx