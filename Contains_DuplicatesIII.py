class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    
        idx = sorted(range(len(nums)), key=lambda x:nums[x])
        sorted_nums = [nums[i] for i in idx]
        print(nums)
        print(idx)
        print(sorted_nums)
        for i in range(len(sorted_nums)-1):
            for j in range(i+1, len(sorted_nums)):
                if abs(sorted_nums[i]-sorted_nums[j]) <=t:
                    if abs(idx[i] - idx[j]) <= k:
                        return True
                else:
                    break

        return False    
    

#Input: nums = [1,2,3,1], k = 3, t = 0
#Output: true

#Input: nums = [1,0,1,1], k = 1, t = 2
#Output: true

#Input: nums = [1,5,9,1,5,9], k = 2, t = 3
#Output: false