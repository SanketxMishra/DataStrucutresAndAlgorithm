class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for idx,val in enumerate(nums):
            diff = target - val

            if diff in hashMap:
                return [idx,hashMap[diff]]
            hashMap[val] = idx