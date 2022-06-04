class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        if m==0:
            return matrix
        n=len(matrix[0])
        print(m,n)
        mat=[]
        temp=[]
        for i in range(n):
            for j in range(m):
                print(i,j)
                temp.append(matrix[j][i])
            mat.append(temp)
            temp=[]
            print(mat)
        return mat
                
        
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[1,4,7],[2,5,8],[3,6,9]]

#Input: matrix = [[1,2,3],[4,5,6]]
#Output: [[1,4],[2,5],[3,6]]