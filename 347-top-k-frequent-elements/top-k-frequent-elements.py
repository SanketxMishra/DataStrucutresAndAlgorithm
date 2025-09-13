class Solution(object):
    def topKFrequent(self, nums, k):
        out = {}
        ret = []
        if len(nums) == 1:
            return nums
        for i in nums:
            if i in out:
                out[i] += 1
            else:
                out[i] = 1
        
        dict_sorted = sorted(out.items(), key=lambda item: item[1], reverse=True)
        
        for i in range(k):
            ret.append(dict_sorted[i][0])
        
        return ret
