class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #using Hash Maptraverse and insertion-O(1)
        #T.C-O(9*9)
        rows=collections.defaultdict(set)
        
        cols=collections.defaultdict(set)
        
        squares=collections.defaultdict(set)
                
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3,j//3)]):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        print(rows,cols,squares)
        return True
                

#Input: board = 
#[["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: false
#Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.