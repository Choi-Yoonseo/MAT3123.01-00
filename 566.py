class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)* len(mat[0]):
            return mat

        final = []
        temp = 0
        c_temp = 0
        row = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if c_temp == c:
                    final.append(list(row))
                    row.clear()
                    c_temp = 0

                row.append(mat[i][j])
                c_temp += 1
        if row:
            final.append(list(row))
        return final
        


                


