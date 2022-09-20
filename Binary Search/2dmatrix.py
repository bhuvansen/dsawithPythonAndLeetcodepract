class Solution:
    def sortedColSortedRow(self, matrix, target):
        r = 0
        c = len(matrix)-1
        while (r<len(matrix)-1 and c>=0):
            if matrix[r][c]==target:
                return [r, c]
            if matrix[r][c]<target:
                r+=1
            else:
                c-=1
        return [-1, -1]
        
    def sortedMatrix(self, matrix, target):
        rowStart = 0
        rowEnd = len(matrix) - 1
        while rowStart <= rowEnd:
            mid = (rowStart + rowEnd) // 2
            if target == matrix[mid][0]:
                return [mid, 0]
            elif target < matrix[mid][0]:
                rowEnd = mid - 1
            else:
                rowStart = mid + 1
        targetRow = rowEnd
        colStart = 1
        colEnd = len(matrix[targetRow])-1
        while colStart <= colEnd:
            mid = (colStart + colEnd) // 2
            if matrix[targetRow][mid] == target:
                return [targetRow, mid]
            elif target < matrix[targetRow][mid]:
                colEnd = mid - 1
            else:
                colStart = mid + 1
        return [-1,-1]

sol = Solution()
matr = [[10,20,30,40],
        [15,25,35,45],
        [28,29,37,49],
        [33,34,38,50]]
print(sol.sortedColSortedRow(matr, 37))
matr2 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        ]   
print(sol.sortedMatrix(matr2, 1))
