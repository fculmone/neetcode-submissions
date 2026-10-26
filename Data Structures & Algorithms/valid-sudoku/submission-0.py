class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validRows() -> bool:
            for i in range(9):
                nums_encountered = set()
                for j in range(9):
                    if board[i][j] in nums_encountered \
                            and board[i][j] != '.':
                        return False
                    else:
                        nums_encountered.add(board[i][j])
            return True

        def validCols() -> bool:
            for i in range(9):
                nums_encountered = set()
                for j in range(9):
                    if board[j][i] in nums_encountered \
                            and board[j][i] != '.':
                        return False
                    else:
                        nums_encountered.add(board[j][i])
            return True

        # i and j are indexes for big squares row + col
        # x and y are offsets for indexes inside big squares
        def validSquares() -> bool:
            for i in range(3):
                for j in range(3):
                    nums_encountered = set()
                    for x in range(3):
                        for y in range(3):
                            if board[i * 3 + x][j * 3 + y] in nums_encountered \
                                    and board[i * 3 + x][j * 3 + y] != '.':
                                return False
                            else:
                                nums_encountered.add(board[i * 3 + x][j * 3 + y])
            return True
        
        return validRows() and validCols() and validSquares()
