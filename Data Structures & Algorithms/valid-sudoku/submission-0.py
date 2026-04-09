class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #- Iterates by matrix
        #- Use a hashmap that use numbers 1-9 as the keys, and a tuple of 2 sets:
        #   p: ({x1,x2,x3,..,xn},{y1,y2,y3,..yn}), p in [1-9], 0 < xi < 9, 0 < yi < 9
        #   This hashmap manages rows and columns.
        #- To verify rows and columnas,for each element position (x,y) verify if:
        #   1.- A row has duplicated elements (x in hashmap[p][0])
        #   2.- A column has duplicated elements (y in hashmap[p][1])
        #-  To verify valid sub-boxes, we use a set that stores the numbers that apapers in the sub-box:
        #       (bx, by) = {n1, n2, n3,..., n9}
        #   if n is in the set, that means that this number is duplicated, and the sub-box is not valid
        cols_rows_hash = defaultdict(lambda: (set(), set()))
        sub_boxes_hash = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                if i in cols_rows_hash[num][0] or j in cols_rows_hash[num][1]:
                    print(num, i, j, 'col or row not valid')
                    return False
                else:
                    cols_rows_hash[num][0].add(i)
                    cols_rows_hash[num][1].add(j)

                actual_box = (i // 3, j // 3)
                if num in sub_boxes_hash[actual_box]:
                    print(num, i, j, 'sub_box not valid')
                    return False
                else:
                    sub_boxes_hash[actual_box].add(num)
        
        return True

                

