class Solution(object):
    def productExceptSelf(self, nums):
        arr = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            arr.append(product)
        return arr  
        