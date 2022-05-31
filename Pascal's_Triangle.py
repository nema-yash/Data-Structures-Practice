class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_list=[[1],[1,1]]
        if numRows==1:
            return final_list[:1]
        if numRows>2:
            for i in range(2,numRows):
                l=[1]
                for j in range(1,i):
                    l.append(final_list[i-1][j-1]+final_list[i-1][j])
                l.append(1)
                final_list.append(l)
        return final_list


#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


#Input: numRows = 1
#Output: [[1]]