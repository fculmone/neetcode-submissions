class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # you can represent any position as a 2d index by multiplying
        # row num by number of columns plus curr column
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        def rc_to_i(r, c):
            return (r * num_cols) + c 
        def i_to_rc(i):
            c = i % num_cols 
            r = (i - c) // num_cols
            return r, c
        # print(i_to_rc(9)) #2, 1
        # print(i_to_rc(3)) # 0, 3
        # print(i_to_rc(7)) # 1, 3
        # print(i_to_rc(4)) # 1, 0
        # print(rc_to_i(2, 1))
        # print(rc_to_i(0, 3))
        # print(rc_to_i(1, 3))
        # print(rc_to_i(1, 0))
        l = 0
        r = num_rows * num_cols - 1
        while l < r:
            middle = (l + r) // 2
            row, col = i_to_rc(middle)
            if matrix[row][col] < target:
                l = middle + 1
            else:
                r = middle
        row, col = i_to_rc(l)
        if matrix[row][col] == target:
            return True
        return False

                
     