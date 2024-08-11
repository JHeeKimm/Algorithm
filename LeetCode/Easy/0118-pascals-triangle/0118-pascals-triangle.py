class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        
        for i in range(1, numRows):
            nextRow = [1] 
            for j in range(i-1):
                nextRow.append(answer[i-1][j]+answer[i-1][j+1])
                
            nextRow.append(1)
            answer.append(nextRow)
        return answer