class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        l=[]
        for i in range(len(nums)):
            if target-nums[i] in h.keys():
                l.append(h[target-nums[i]])
                l.append(i)
                return l
            h[nums[i]]=i
        return l