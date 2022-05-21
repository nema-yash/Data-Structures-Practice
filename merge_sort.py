class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        import operator
        compare = operator.lt 
        if m < 1: 
            nums1[:]=nums2
        elif n<1:
            nums1[:]=nums1[:m]
        else: 
            left = nums1[:m] 
            right = nums2 
            result = [] 
            i,j = 0, 0 
            while i < m and j < n: 
                if compare(left[i], right[j]): 
                    result.append(left[i]) 
                    i += 1 
                    print(i,result)
                else: 
                    result.append(right[j]) 
                    j += 1 
                    print(j,result)
            while (i < m): 
                result.append(left[i]) 
                i += 1 
                print(i,result)
            while (j < n): 
                result.append(right[j]) 
                j += 1 
                print(j,result)
            nums1[:]=result
            
#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]
#Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


#Input: nums1 = [1], m = 1, nums2 = [], n = 0
#Output: [1]
#Explanation: The arrays we are merging are [1] and [].
#The result of the merge is [1].


#Input: nums1 = [0], m = 0, nums2 = [1], n = 1
#Output: [1]
#Explanation: The arrays we are merging are [] and [1].
#The result of the merge is [1].
#Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.