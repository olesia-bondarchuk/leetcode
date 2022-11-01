from  typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        result = [[1]]

        for i in range(1, numRows):
            row = []
            for j in (0, i+1):
                if j in (0, i):
                    row.append(1)
                else:
                    row.append(result[i-1][j-1] + result[i-1][j])

            result.append(row)
        return result
