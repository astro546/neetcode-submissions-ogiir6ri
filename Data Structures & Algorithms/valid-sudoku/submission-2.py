class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(n^2)
        # This solution uses bitwise operation, and works with bitmaps for columns, rows and sub-boxes

        rows = [0] * 9
        cols = [0] * 9
        sub_boxes = [0] * 9
        for i in range(9):
            for j in range(9):
                if  board[i][j] == '.':
                    continue

                val = int(board[i][j]) - 1
                cur_bit = 1 << val
                if (cur_bit & rows[i]) or (cur_bit & cols[j]) or (cur_bit & sub_boxes[(i // 3) * 3 + (j // 3)]):
                    print(board[i][j], rows, cols, sub_boxes)
                    return False
                
                rows[i] |= cur_bit
                cols[j] |= cur_bit
                sub_boxes[(i // 3) * 3 + (j // 3)] |= cur_bit

        return True


                

                

