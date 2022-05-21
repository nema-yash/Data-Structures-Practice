class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=-inf
        ans=-inf
        for i in nums:
            sum= max(i,sum+i)
            ans=max(ans,sum)
        return ans
    

#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.
    
#Input: nums = [1]
#Output: 1
    
#Input: nums = [1]
#Output: 1
        