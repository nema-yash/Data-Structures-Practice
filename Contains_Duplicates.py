class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    #Creating function to check duplicates and return True if Duplicates exist. 
    #Set functions reads all unique characters, so len of set function and len of string should be different for duplicates to exist
        if len(set(nums))!=len(nums):
            return True
        else:
            return False

#Test Cases        
#Input: nums = [1,2,3,1]
#Output: true

#Input: nums = [1,2,3,4]
#Output: false

#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true
