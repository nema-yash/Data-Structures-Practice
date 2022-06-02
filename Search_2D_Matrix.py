class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        b=[i[0] for i in matrix]
        print(b)
        
        if target<b[0]:
            return False
        elif target in set(matrix[0]):
            return True
        elif target>matrix[len(b)-1][-1]:
            return False
        elif target in set(matrix[len(b)-1]):
            return True
        else:
            j=-1
            for i in range(1,len(b)):
                if ((target>=b[i-1]) and (target<b[i])):
                    j= (i-1)
                    print(j)
                    break
                elif i==len(b)-1 and target>b[i]:
                    j= (i)
                    print(j)
                    break
                else:
                    print(j)
                    print("keep trying")
        
            if j!=-1:
                if target in set(matrix[j]):
                    return True
            return False
            
        
        #find row number - create list with first elements of col0, apply binary search
        
        #check availability - In the selected row- use contain
        
        
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true

#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: false