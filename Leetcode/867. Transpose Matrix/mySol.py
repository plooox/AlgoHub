class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(len(matrix[0])):
            row = [matrix[j][i] for j in range(len(matrix))]
            answer.append(row)
        return answer
