class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #O(log(m*n))
        #This solution treats the matrix like a 1D array
        #The map for convert mid index to (i,j) coordinates is: 
        #   (mid // n, mid % n), n = number of columns
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            i,j = mid // n, mid % n 
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                r = mid - 1
            else:
                l = mid + 1
        return False
        