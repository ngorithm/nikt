class Solution(object):
    def moveZeroes(self, nums):
        c = 0
        for i in range(len(nums)):
            if nums[i]!= 0:  
                nums[c],nums[i] = nums[i],nums[c]
                c+=1  