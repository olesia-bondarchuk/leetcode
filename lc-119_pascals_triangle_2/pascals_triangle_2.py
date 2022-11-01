from  typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex is None:
            return []

        result = [1]

        for i in range(1, rowIndex+1):
            row = []
            for j in range(0, i+1):
                if j in (0,i):
                    row.append(1)
                else:
                    row.append(result[j-1] + result[j])

            result = row
        return result
