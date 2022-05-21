class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        a=[]
        for i, num in enumerate(nums):
            if target-num in index:
                a.append(index[target-num])
                a.append(i)
                return a
            index[num] = i
                
        

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

#Input: nums = [3,2,4], target = 6
#Output: [1,2]        