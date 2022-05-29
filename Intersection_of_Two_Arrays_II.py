class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i)
        return result


#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]

#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
#Explanation: [9,4] is also accepted.

