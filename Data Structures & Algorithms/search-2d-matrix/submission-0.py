class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Find the row with binary search
        #Once i have the row, if the target_row != -1, search the target column with binary search
        left_row = 0
        right_row = len(matrix) - 1
        target_row = -1
        while left_row <= right_row:
            mid_row = left_row + (right_row - left_row)//2
            if matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]:
                target_row = mid_row
                break
            elif target > matrix[mid_row][-1]:
                left_row = mid_row + 1
            else:
                right_row = mid_row - 1
                
        if target_row == -1: return False

        left_col = 0
        right_col = len(matrix[0]) - 1
        while left_col <= right_col:
            mid_col = left_col + (right_col - left_col)//2
            if matrix[target_row][mid_col] == target:
                return True
            elif target > matrix[target_row][mid_col]:
                left_col = mid_col + 1
            else:
                right_col = mid_col - 1
        return False