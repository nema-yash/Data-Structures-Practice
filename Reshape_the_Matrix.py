class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = sum(mat, [])     
        if r*c != len(flat):
            return mat
        return [flat[i:i+c] for i in range(0, len(flat), c)]
    
    
#Input: mat = [[1,2],[3,4]], r = 1, c = 4
#Output: [[1,2,3,4]]

#Input: mat = [[1,2],[3,4]], r = 2, c = 4
#Output: [[1,2],[3,4]]