class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    #Creating function to check duplicates and return True if Duplicates exist. 
    #Set functions reads all unique characters, so len of set function and len of string should be different for duplicates to exist
        if len(set(nums))!=len(nums):
            return True
        else:
            return False