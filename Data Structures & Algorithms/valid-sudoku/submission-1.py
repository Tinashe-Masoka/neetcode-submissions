class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board :
            if not self.isCountValid(row) : return False
        
        # Create columns array of arrays
        Columns = [ [] for _ in range(9) ]
        for i in range(9) :
            Columns[i].append(board[0][i])
            Columns[i].append(board[1][i])
            Columns[i].append(board[2][i])
            Columns[i].append(board[3][i])
            Columns[i].append(board[4][i])
            Columns[i].append(board[5][i])
            Columns[i].append(board[6][i])
            Columns[i].append(board[7][i])
            Columns[i].append(board[8][i])
        
        for column in Columns :
            if not self.isCountValid(column) : return False

        #Create 3x3 array of arrays
        Square3x3 = [ [] for _ in range(9) ]
        for i in range(0,7,3) :
            Square3x3[i].append(board[0][i])
            Square3x3[i].append(board[0][i+1])
            Square3x3[i].append(board[0][i+2])
            Square3x3[i].append(board[1][i])
            Square3x3[i].append(board[1][i+1])
            Square3x3[i].append(board[1][i+2])
            Square3x3[i].append(board[2][i])
            Square3x3[i].append(board[2][i+1])
            Square3x3[i].append(board[2][i+2])

            Square3x3[i+1].append(board[3][i])
            Square3x3[i+1].append(board[3][i+1])
            Square3x3[i+1].append(board[3][i+2])
            Square3x3[i+1].append(board[4][i])
            Square3x3[i+1].append(board[4][i+1])
            Square3x3[i+1].append(board[4][i+2])
            Square3x3[i+1].append(board[5][i])
            Square3x3[i+1].append(board[5][i+1])
            Square3x3[i+1].append(board[5][i+2])

            Square3x3[i+2].append(board[6][i])
            Square3x3[i+2].append(board[6][i+1])
            Square3x3[i+2].append(board[6][i+2])
            Square3x3[i+2].append(board[7][i])
            Square3x3[i+2].append(board[7][i+1])
            Square3x3[i+2].append(board[7][i+2])
            Square3x3[i+2].append(board[8][i])
            Square3x3[i+2].append(board[8][i+1])
            Square3x3[i+2].append(board[8][i+2])
        
        for square in Square3x3 :
            if not self.isCountValid(square) : return False

        return True

    def isCountValid(self, nums: List[str]) -> bool:
        nums_dict = {}
        for num in nums :
            if num == "." : continue
            nums_dict[num] = nums_dict.get(num,0) + 1
            if nums_dict[num] > 1 :
                return False
        return True




