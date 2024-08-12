class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        
        for i in range(1, rowIndex+1):
            nextRow = [1]
            for j in range(1, i):
                nextRow.append(triangle[i-1][j-1]+triangle[i-1][j])
                
            nextRow.append(1)
            triangle.append(nextRow)
        return triangle[rowIndex]